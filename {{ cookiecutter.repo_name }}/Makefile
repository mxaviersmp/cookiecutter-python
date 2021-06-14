help:
	@echo "available commands"
	@echo " - venv              : creates the development environment"
	@echo " - clean             : clean temporary folders and files"
	@echo " - lint              : checks code style and type checks"
	@echo " - test              : runs all unit and integration tests"
	@echo " - coverage          : runs coverage report"
	@echo " - clean-all         : removes environment, volumes, containers and images"

venv:
	[ -d "./env" ] || ( \
		python -m venv env && \
		. env/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements-dev.txt && \
		pip install -e . && \
		pre-commit install && \
		((command -v gitmoji >/dev/null && gitmoji -i) || echo Please install gitmoji-cli) \
	)
	touch env/bin/activate

clean:
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name .mypy_cache`
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .ipynb_checkpoints`
	rm -f .coverage

lint: venv clean
	. env/bin/activate; flake8; mypy

test: venv clean
	. env/bin/activate; pytest

coverage: venv clean
	. env/bin/activate; coverage run -m pytest; coverage report

clean-all: clean
	rm -rf app.egg-info
	rm -rf env
