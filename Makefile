docker.build:
	docker-compose build --force-rm

docker.start:
	docker-compose up

docker.stop:
	docker-compose down

migrate:
	docker-compose python manage.py migrate

makemigrations:
	docker-compose python manage.py makemigrations

install:
	poetry install

install:
	django install

