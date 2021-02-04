brain-games:
	poetry run brain-games

install:
	poetry install

build:
	poetry build

package-install:
	pip install --user dist/*.whl

package-uninstall:
	pip uninstall hexlet-code

lint:
	poetry run flake8 brain_games

