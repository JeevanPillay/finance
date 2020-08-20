MODULE := app

init:
	python3 setup.py install

test:
	@pytest

run:
	@python -m $(MODULE)

lint:
	echo "none"

venv-unix:
	python3 -m venv venv

venv-windows:
	py -3.7 -m venv venv
