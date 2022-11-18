VENV ?= ./.venv
PIPFILE ?= Pipfile
PY_VERSION ?= 3.10

init: ## init and install packages optional: dev=1 set export PIPENV_VENV_IN_PROJECT = true
	export PIPENV_VENV_IN_PROJECT=1
	pipenv --python $(PY_VERSION)
	pipenv install

shell: ## Run pipenv shell with python version
	pipenv shell --python $(PY_VERSION)

run: ## Runs uvicorn main:app --reload
	pipenv run uvicorn app.main:app --reload

clean: ## Remove VENV __pycache__
	find . | grep -E "(__pycache__$|\.pyc$|\.pyo$ )" | xargs rm -rf
	pipenv --rm
	# rm -rf $(VENV)

test: ## Runs unit tests using pytest
	pipenv run pytest

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
