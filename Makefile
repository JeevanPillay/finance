venv-unix:
	python3 -m venv <env_name>

venv-windows:
	py -3.7 -m venv flatenv

init:
	python3 setup.py install

run:
	echo "run files here"

test:
	echo "test scripts here"
