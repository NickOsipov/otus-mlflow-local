include .env

down:
	docker-compose down

build:
	docker-compose build

up:
	docker-compose up -d --build

re-up: down up

run-pipe:
	python3 src/pipeline.py --config exp/ml_config.yaml

load-model:
	python3 src/load_model.py --model-alias champion