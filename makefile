GAME?=brain_games

install:
	@poetry install

lint:
	@poetry run flake8 brain_games

build:
	@poetry build

publish: build
	@poetry publish -r testpypi

run:
	@poetry run python -m brain_games.scripts.$(GAME)

.PHONY: install lint build publish
