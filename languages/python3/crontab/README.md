# Crontab

## Architecture
- **__init__py**:           Empty file to signify this directory is a python module.
- **crontab.py**:           The source code
- **README.md**:            This file
- **requirements.txt**:     List of python dependencies
- **requirements-dev.txt**: List of python dependencies for develop and make tests
- **test_crontab.py**:      Code containing all tests

## Install

On terminal, in this directory run:
```bash
pip install -r requirements.txt
```
## Usage

Run the program from terminal
```bash
# Run
python ./crontab.py
```

Read the help and test different options/arguments combination.

## Unit test

Unit test are run with pytest

### Install dependencies

On terminal, in this directory run:
```bash
pip install -r requirements-dev.txt
```

### Run

Go in this directory and run these commands:
```bash
# Run tests
pytest
```