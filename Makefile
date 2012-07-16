run:
	venv/bin/python manage.py runserver

install:
	virtualenv ./venv --no-site-packages
	venv/bin/pip install -r requirements.txt
