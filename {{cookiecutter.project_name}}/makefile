DOCKER_NAME?={{cookiecutter.project_name}}
DOCKER_TAG?=latest
ENV_FILE?=.env
CI_PROJECT_DIR?=./

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help:
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

install: install-lib-register ##Install in pipeline
install:

	pip install .

install-deps-dev:  install-lib-register ##Install in pipeline
install-deps-dev:
	
	pip install -e .[dev]

clean: ## Remove build and cache files
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	# Remove all pycache
	find . | grep -E '(__pycache__|\.pyc|\.pyo$$)' | xargs rm -rf

lint: install-deps-dev ## Runs flake8 on src, exit if critical rules are broken
lint:
	# stop the build if there are Python syntax errors or undefined names
	ruff check

lint-fix: install-deps-dev ## Runs flake8 on src, exit if critical rules are broken
lint-fix:
	# stop the build if there are Python syntax errors or undefined names
	ruff check --fix

test: ## Run pytest
test:

	python3 -m pytest --cov-report xml:$(CI_PROJECT_DIR)/reports/coverage.xml --cov-report html:$(CI_PROJECT_DIR)/reports/html/ --cov-report json:$(CI_PROJECT_DIR)/reports/coverage.json --cov-config $(CI_PROJECT_DIR)/pyproject.toml

install-lib-register: ## Install git package register additional
install-lib-register:


compile-deps: ## Compile dependencies requirements.in -> requirements.txt 
compile-deps:
	pip-compile --no-emit-index-url --no-emit-trusted-host

run-docker-local: ## build, start and run docker image locally
run-docker-local: 
	docker run --env-file $${ENV_FILE} -it $(DOCKER_NAME):$(DOCKER_TAG)  sh

build-image-local: ## Build docker image locally
build-image-local:
	docker build --secret id=netrc,src=${HOME}/.netrc  -t $(DOCKER_NAME):$(DOCKER_TAG) -f Dockerfile .

