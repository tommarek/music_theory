SRC_CORE=src
SRC_TEST=tests

PYTHON=venv/bin/python3
PIP=venv/bin/pip3
PYLINT=venv/bin/pylint
COVERAGE=venv/bin/coverage
PUR=venv/bin/pur

all: venv run

help:
	@echo "Some available commands:"
	@echo " * run          - Run code."
	@echo " * venv         - Create/run venv, install requrements"
	@echo " * test         - Run unit tests and test coverage."
	@echo " * clean        - Cleanup (e.g. pyc files)."
	@echo " * lint         - Check code lints (pylint)."
	@echo " * deps-update  - Update dependencies (pur)."
	@echo " * deps-create  - Create dependencies (pipreqs)."

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	@test -d venv || virtualenv venv -p python3.7
	@$(PIP) install -Ur requirements.txt
	@touch venv/bin/activate

run: venv
	@$(PYTHON) $(SRC_CORE)/run.py


clean:
	rm -rf venv
	find -iname "*.pyc" -delete

test: venv
	@$(COVERAGE) run --source . -m $(SRC_TEST).test_hello
	@$(COVERAGE) report

lint: venv
	@$(PYLINT) $(SRC_CORE)

deps-update: venv
	@$(PUR) -r requirements.txt

deps-create:
	@pipreqs --use-local --force .

test-ci:
	$(COVERAGE) run --source . -m $(SRC_TEST).test_hello
	@$(COVERAGE) report

lint-ci:
	@$(PYLINT) $(SRC_CORE)
