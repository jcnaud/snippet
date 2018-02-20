# Doctest

## Mode 1 : Run doctest from code
You can run doctest from code with this line in **main.py**
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
Now, run the code:
```bash
python main.py
```
Or with verbose mode to see the traitement in background
```bash
python -v main.py
```

## Mode 2 : Run doctest from command line
Disable doctest from code with the following line in **main.py**
```python
if __name__ == "__main__":
    pass
    #import doctest
    #doctest.testmod()
```
Now, run with command line:
```bash
python -m doctest main.py
```
Or with verbose mode to see the traitement in background
```bash
python -m doctest -v main.py
```