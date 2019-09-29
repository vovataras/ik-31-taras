.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	# Ваш код тут
	pip install pipenv
	pipenv --python 3.7
	pipenv install requests
	pipenv install ntplib

test:
	@echo "Start tests."
	# Ваш код тут
	pipenv run pytest tests/tests.py > results.txt

run:
	@echo "Run Python app."
	# Ваш код тут
	pipenv run python app.py >> results.txt

deploy:
	@echo "Adding and Committing results.txt to git."
	# Ваш код тут
	git add results.txt
	git commit -m "Lab_2: Commit from make"
	git push