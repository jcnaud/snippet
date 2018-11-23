# Jupyter

Jupyter is a notebook (web programming interface) design to make data science programming and visualisation.
Jupyter is a package integrated in Anacanda (python tree repositories)
This tree repositories is manage by Conda (package manager)

You can install multiple tree in conda.

Anacanda agregate all usefull data science librarie and check if they are compatible in each other.


## Install

Download Anaconda on [https://www.anaconda.com/download/](https://www.anaconda.com/download/).

Now, you have different exe:
- Anaconda Navigator : Gui to manage conda envs (create or install package)
- Anaconda Prompt: CMD (command prompt) executed in conda default tree.
- Jupyter Notebook: Run note book server and open web connected to it.
- Spyter: Python/Anaconda IDE.

You can also connect to anaconda on cmd:


```cmd
cd  anaconda3\Scripts
conda env list
activate base
```


## Jupiter codeonfiguration

###  Generate jupyter configuration file if it not exist.

Open Anaconda Prompt
```cmd
jupyter notebook --generate-config
```

Edite the file **%userprofile%/.jupyter/jupyter_notebook_config.py**

Modify this line to make jupyter run in the choising directiry
```python
c.NotebookApp.notebook_dir = 'C:/var'
```

## You can install additionnal package like
```ipython
!pip install plotly
!pip install py_d3
```
