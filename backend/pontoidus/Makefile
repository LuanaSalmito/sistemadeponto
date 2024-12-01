IMAGE_NAME=my_django_app


COMPOSE_PROJECT_NAME=myproject

build:
	docker build -t $(IMAGE_NAME) .

start:
	docker-compose up

clean:
	docker-compose down --volumes --rmi all

migrate:
	docker-compose run web python manage.py migrate

test:
	docker-compose run web python manage.py test

createsuperuser:
	docker-compose run web python manage.py createsuperuser
