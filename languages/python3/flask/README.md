# Flask


## Context
Flask is a samll web framework to make API REST 

## Dependancy of this snippet
Intall dependancy of this project:
```bash
pip install -r requirements.txt
```

## Run
Run simple.py:
```bash
FLASK_APP=simple.py flask run
```

The api run on http://127.0.0.1:5000/


## Informations

- ```@pytest.yield_fixture``` is deprecated in favour fo ```@pytest.fixture```
- yield ```@pytest.fixture``` break decorator like ```@requests_mock.mock()```
- With yield ```@pytest.fixture```, use mock like context (```with```) in test function or in yield function
