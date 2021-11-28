build:
	poetry build

install:
	poetry install

lint:
	poetry run flake8 gendiff

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

.PHONY: build install lint package-install publish