install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

run:
	python manage.py runserver

createuser:
	python manage.py createsuperuser

migrate:
	python manage.py makemigrations

migrate:
	python manage.py migrate

build:
	docker build . -t mysite

run-docker:
	docker run -p 8080:8000 mysite

venv:
	source ~/.django/bin/activate
