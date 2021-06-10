help:
	@echo "available commands"
	@echo " - dev       : install development environment"
	@echo " - clean     : clean temporary folders and files"
	@echo " - lint      : checks code style"
	@echo " - test      : runs all unit tests"
	@echo " - coverage  : runs coverage report"
	@echo " - doc       : creates documentation in html"

dev:
	pip install -r requirements-dev.txt
	pip install -e .
	pre-commit install
	(command -v gitmoji >/dev/null && gitmoji -i) || echo Please install gitmoji-cli

clean:
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .ipynb_checkpoints`
	rm -rf docs/_build
	rm -f .coverage

lint: clean
	flake8
	mypy

test: clean
	pytest

coverage: clean
	coverage run -m pytest
	coverage report

doc: clean
	rm -rf docs/api docs/examples
	sphinx-apidoc -f -o docs/references {{ cookiecutter.project_src }} {{ cookiecutter.project_src }}/tests/
	jupyter nbconvert --to rst --output-dir docs/examples notebooks/[0-9]*.ipynb
	make -C docs html
