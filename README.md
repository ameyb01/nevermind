# NeverMind

Experiment tracking service. Because someone has to remember.

A production-style backend for logging, querying, and comparing ML experiment runs.

## Tech Stack
Python, FastAPI, PostgreSQL, SQLAlchemy, Redis, RQ, Docker, AWS EC2

## Features
- Create and manage experiments
- Log runs with metrics, configs, and tags
- Compare runs by metric — top-k, average, failure rate
- Async job processing via Redis + RQ
- Fully Dockerized local setup

## Run Locally
git clone https://github.com/ameyb01/nevermind
cd nevermind
docker-compose up --build

## API Docs
http://localhost:8000/docs
