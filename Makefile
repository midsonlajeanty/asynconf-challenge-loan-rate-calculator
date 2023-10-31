.PHONY: env clean migrate test run install freeze force-reset-migrations


VENV_NAME?=venv
PYTHON=$(VENV_NAME)/bin/python
PIP=$(VENV_NAME)/bin/pip

HOST=127.0.0.1
PORT=8000

run:
	$(PYTHON) manage.py runserver $(HOST):$(PORT)

env:
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt

freeze:
	$(PIP) freeze > requirements.txt

clean: freeze
	rm -rf $(VENV_NAME)
	rm -rf db.sqlite3
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

force-reset-migrations: clean
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	find . -not -path "./$(VENV_NAME)/*" -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -not -path "./$(VENV_NAME)/*" -path "*/migrations/*.pyc" -delete

test:
	$(PYTHON) manage.py test

install: env migrate
