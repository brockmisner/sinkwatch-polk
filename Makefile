.PHONY: lint test typecheck db-up db-migrate

lint:
	ruff check src tests apps

test:
	pytest -q

typecheck:
	mypy src

db-up:
	docker compose up -d postgis minio mlflow

db-migrate:
	alembic upgrade head
