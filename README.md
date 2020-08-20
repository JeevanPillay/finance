# Python Template

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

3. Install the Python environment: `cd <yourdir>` -- if not already in it, then run the set-up script, `python setup.py install`, which will install the dependencies and the environment.

4. Test that the installation works by running < in the command line. Note that closing the window does not stop the program. To exit, use ctrl-c, until it prints out Aborted!
