# Python Template

# Configuration
First, follow these instructions to set up your environment to prepare the Flatland environment on your local machine.

Download and install Python 3.7.8, if not installed yet.
```
https://www.python.org/downloads/release/python-378/
```

## Setting up the template
1. Go to `setup.py` and change the configuration to reflect the new repository's information.
2. Change the `Makefile` settings dependent on the configurations that are required.
  - ensure that the venv -> `<env_name>` is added to `.gitignore`.
3. Add dependencies in `requirements.txt`.
4. Go to `.github/workflows` and update documents depending on the projects name.

## Building the Project
1. **Recommended**: `Make venv-<os>` -- this should create the virtual environment -- see `venv-windows` and `venv-unix` in `Makefile` for more information,
  - (Every time) Activate the virtual environment to use it in command line:
    - Windows: `cd <yourdir>`, then `<env_name>\Scripts\activate`
    - Unix-like: `cd <yourdir>`, then `source ./<env_name>/bin/activate`
  - In your IDE such as Eclipse PyDev or PyCharm, select the Python interpreter in the
    `<env_name>/bin` or `<env_name>/Scripts` directory for your assignment project.
    - Note, the virtual environment shouldn't be pushed onto GitHub -- add to `.gitignore` if haven't already.
2. Run the `Make init` command that will initiate the `setup.py` file -- install dependencies and set's up the entire project.

## Run the Project
- Add information into `Make run` to ensure that you can run application with make.

## Adding dependencies
- `pip install <your-package>` and add to `requirements.txt` if needed.



# Included Tools
1. Virtual Environment
2. GitHub Actions
3. Python 3.7.8
4. Makefile -- for fast installation
