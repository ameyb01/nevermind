from sqlalchemy.orm import Session
from app.models.run import Run, RunStatus
from app.schemas.run import RunCreate
from fastapi import HTTPException
from typing import Any

def create_run(db: Session, data: RunCreate) -> Run:
    run = Run(
        experiment_id=data.experiment_id,
        status=data.status,
        metrics=data.metrics,
        config=data.config,
        tags=data.tags
    )
    db.add(run)
    db.commit()
    db.refresh(run)
    return run

def list_runs(db: Session, experiment_id: str) -> list[Run]:
    return db.query(Run).filter(
        Run.experiment_id == experiment_id
    ).order_by(Run.created_at.desc()).all()

def compare_runs(
    db: Session,
    experiment_id: str,
    metric: str,
    top_k: int = 5
) -> dict[str, Any]:
    runs = db.query(Run).filter(
        Run.experiment_id == experiment_id,
        Run.status == RunStatus.success
    ).all()

    if not runs:
        raise HTTPException(status_code=404, detail="No successful runs found")

    # filter runs that actually have the metric
    runs_with_metric = [
        r for r in runs
        if r.metrics and metric in r.metrics
    ]

    if not runs_with_metric:
        raise HTTPException(status_code=404, detail=f"No runs found with metric: {metric}")

    # sort by metric descending
    sorted_runs = sorted(
        runs_with_metric,
        key=lambda r: r.metrics[metric],
        reverse=True
    )

    top_runs = sorted_runs[:top_k]

    metric_values = [r.metrics[metric] for r in runs_with_metric]
    avg_metric = sum(metric_values) / len(metric_values)

    total = len(runs)
    failed = db.query(Run).filter(
        Run.experiment_id == experiment_id,
        Run.status == RunStatus.failed
    ).count()
    failure_rate = round(failed / total, 3) if total > 0 else 0.0

    return {
        "experiment_id": experiment_id,
        "metric": metric,
        "top_runs": [
            {
                "id": r.id,
                "metrics": r.metrics,
                "config": r.config,
                "tags": r.tags,
                "created_at": r.created_at.isoformat()
            }
            for r in top_runs
        ],
        f"average_{metric}": round(avg_metric, 4),
        "failure_rate": failure_rate,
        "total_runs": total
    }