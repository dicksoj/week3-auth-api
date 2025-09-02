.PHONY: build up down logs test lint push

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	pytest -v tests

lint:
	flake8 app

push:
	docker build -t ghcr.io/dicksoj/auth-api:latest .
	docker push ghcr.io/dicksoj/auth-api:latest
