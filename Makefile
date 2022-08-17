clean:
	pipenv --rm 

clean-pyc:
	find . -name \*.pyc -delete

prepare-dev:
	pipenv install --dev
	pipenv run pre-commit install 

lint:
	pipenv run black . 
	pipenv run flake8 

check:
	pipenv run black --check .
	pipenv run flake8

test: clean-pyc 
	pipenv run pytest --junitxml=test/report.xml --cov=src/ --cov-report xml:test/coverage.xml

run:
	pipenv run python main.py
