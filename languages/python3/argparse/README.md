# Argparse

## Architecture

- **cli.py**:               The source code
- **README.md**:            This file
- **requirements.txt**:     List of python dependencies
- **requirements-dev.txt**: List of python dependencies for develop and make tests
- **test_cli.py**:          Code containing all tests

## Install

Nothing to do, all package used are python default packages.
The requirements.txt is empty.

## Usage

Run the program from terminal
```bash
# Display help
python ./cli.py -h
# Typical usage
python ./cli.py -f config.yml -m 2 file_1 file_2 file_3
```

Read the help and test different options/arguments combination.

## Unit test

Unit test are run with pytest

### Install dependencies

```bash
pip install -r requirements-dev.txt
```

### Run

Go in this directory and run these commands:
```bash
# Run tests
pytest
```