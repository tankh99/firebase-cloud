PYTHON = python

setup:
	cd src && $(PYTHON) -m venv venv

install:
	source src/venv/bin/activate && pip install -r src/requirements.txt

start-local:
	source src/venv/bin/activate && firebase emulators:start