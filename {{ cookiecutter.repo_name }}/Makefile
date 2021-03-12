clean:
	rm -rf `find . -type d -name .pytest_cache`
	rm -rf `find . -type d -name __pycache__`
	rm -rf `find . -type d -name .ipynb_checkpoints`
	rm -rf docs/_build
	rm -f .coverage

test: clean
	coverage run -m pytest
	coverage report

lint: clean
	flake8

doc: clean
	make -C docs html
