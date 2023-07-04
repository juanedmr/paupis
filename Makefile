install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

run:
	python manage.py runserver

createuser:
    python manage.py createsuperuser