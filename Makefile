clean:
	pipenv --rm

clean-pyc:
	find . -name \*.pyc -delete

clean:
	pipenv --rm

prepare-dev:
	pipenv install --dev
	pipenv run pre-commit install
	pipenv run pip install -e .

lint:
	pipenv run black .
	pipenv run flake8

check:
	pipenv run black --check .
	pipenv run flake8

test: clean-pyc
	pipenv run pytest --junitxml=test/report.xml --cov=answerator/ --cov-report xml:test/coverage.xml

run:
	pipenv run python main.py
