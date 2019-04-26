distribute, setuptools, distutils ou Distutils2.


source : https://pythonhosted.org/an_example_pypi_project/setuptools.html
example : https://github.com/pypa/sampleproject


MANIFEST documentation : https://docs.python.org/2/distutils/sourcedist.html#manifest-template
Classifiers list : https://pypi.org/pypi?%3Aaction=list_classifiers

## Test
Test the setup.py localy
```bash
python setup.py install
```

## Publish on Pypi

```bash
python setup.py register
```

```bash
python setup.py sdist upload
```
