include .env

down:
	docker-compose down

build:
	docker-compose build

up:
	docker-compose up -d --build

re-up: down up