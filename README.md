# Python Template

# Configuration
## Setting up the template
1. Go to `setup.py` and change the configuration to reflect the new repository's information.
2. Change the `Makefile` settings dependent on the configurations that are required.
  - ensure that the venv -> `<env_name>` is added to `.gitignore`.
3. Add dependencies in `requirements.txt`.
4. **Recommended**: `Make virtualenv` -- this should create the virtual environment.
  - (Every time) Activate the virtual environment to use it in command line:
    - Windows: `cd <yourdir>`, then `<env_name>\Scripts\activate`
    - Unix-like: `cd <yourdir>`, then `source ./<env_name>/bin/activate`
  - In your IDE such as Eclipse PyDev or PyCharm, select the Python interpreter in the
    `<env_name>/bin` or `<env_name>/Scripts` directory for your assignment project.
    - Note, the virtual environment shouldn't be pushed onto GitHub -- add to `.gitignore` if haven't already.
5. Run the `Make init` command that will initiate the `setup.py` file.

## Running Files
1. Run `Make run` to run the python main application.

## Adding dependencies
- `pip install <your-package>` and add to `requirements.txt` if needed.

# Manual Configuration
## Setting up your environment -- Python 3.7.8

First, follow these instructions to set up your environment to prepare the Flatland environment on your local machine.

1. Download and install Python 3.7.8, if not installed yet.
```
https://www.python.org/downloads/release/python-378/
```

2. **Recommended**: Use a virtual environment to manage your packages and installation without affecting your regular Python installation,
  - (Once) Create a virtual environment inside your directory
    - Windows: `cd <yourdir>`, then `py -3.7 -m venv <env_name>`
    - Unix-like: `cd <yourdir>`, then `python3 -m venv <env_name>`
  - (Every time) Activate the virtual environment to use it in command line:
    - Windows: `cd <yourdir>`, then `<env_name>\Scripts\activate`
    - Unix-like: `cd <yourdir>`, then `source ./<env_name>/bin/activate`
  - In your IDE such as Eclipse PyDev or PyCharm, select the Python interpreter in the
  `<env_name>/bin` or `<env_name>/Scripts` directory for your assignment project.
  - Note, the virtual environment shouldn't be pushed onto GitHub -- add to `.gitignore`

3. Install the Python environment: `cd <yourdir>` -- if not already in it, then run the set-up script, `python setup.py install`, which will install the dependencies and the environment.

4. Test that the installation works by running < in the command line. Note that closing the window does not stop the program. To exit, use ctrl-c, until it prints out Aborted!
