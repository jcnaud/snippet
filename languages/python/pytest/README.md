# Pytest


## Context
Use **pytest** instead **unittest**

Target : testing **mymodule.py** with **test_mymodule.py**

Constraint on pytest :
 - the file with testing function need to start with the name **test_** (Ex: test_mymodule.py)
 - function in **test_mymodule.py** need to start with the name **test_** (Ex: test_format_message.py)

## Dependancy of this snippet
Intall dependancy of this project:
```bash
pip install -r requirements.txt
```

## Run pytest
Move in the directory where they are file test_*:

Run it:
```bash
pytest
```

## Mock
This snippet have an example of mock.
Mock the **requests** package to allow this test without internet connection


## Informations

- ```@pytest.yield_fixture``` is deprecated in favour fo ```@pytest.fixture```
- yield ```@pytest.fixture``` break decorator like ```@requests_mock.mock()```
- With yield ```@pytest.fixture```, use mock like context (```with```) in test function or in yield function
