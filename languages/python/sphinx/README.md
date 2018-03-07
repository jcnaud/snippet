# sphinx

## Install 
This command install **sphinx** documentation and good theme with **sphinx_rtd_theme**

```bash
pip install -r requirements.txt
```

## Generate documentation for this project

### Compile doc
```bash
cd doc
make html
```

### Display doc
Use web browser to open **build/html/index.html**


## Generate new project
If the project is empty (**not this one**), use this :

```bash
mkdir doc
cd doc
echo "!.gitignore
/build" > .gitignore
sphinx-quickstart .
```

| Question                                                | Reponse |
|-------------------------------------------------------- |-------- |
| Separate source and build directories (y/n) [n]:        | y |
| Name prefix for templates and static dir [_]:           | Enter |
| Project name:                                           | Project test      |
| Author name(s):                                         | Jean-Charles Naud |
| Project release []:                                     | 0.0.1 |
| Project language [en]:                                  | Enter |
| Source file suffix [.rst]:                              | Enter |
| Name of your master document (without suffix) [index]:  | Enter |
| Do you want to use the epub builder (y/n) [n]:          | Enter |
| autodoc: automatically insert docstrings from modules (y/n) [n]:                | y       |
| doctest: automatically test code snippets in doctest blocks (y/n) [n]:          | y       |
| intersphinx: link between Sphinx documentation of different projects (y/n) [n]: | Enter   |
| todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:      | Enter   |
| coverage: checks for documentation coverage (y/n) [n]:                          | y       |
| imgmath: include math, rendered as PNG or SVG images (y/n) [n]:                 | y       |
| mathjax: include math, rendered in the browser by MathJax (y/n) [n]:            | y       |
| ifconfig: conditional inclusion of content based on config values (y/n) [n]:    | y       |
| viewcode: include links to the source code of documented Python objects (y/n) [n]:    | y |
| githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: | Enter |
| Create Makefile? (y/n) [y]:               | Enter |
| Create Windows command file? (y/n) [y]:   | Enter |



### Modify **./doc/source/conf.py** :

#### Import code
To load code, you need to import it and reference it.
For example to import **./mymodule/mymodule**, add these liens at begining of **conf.py** :
```bash
import os
import sys
sys.path.insert(0, os.path.abspath('../../mymodule'))
```
Now it is possible to reference on these modules or class in *.rst documentation (We see it after)


#### Change theme

Change the line **html_theme** with :
```
html_theme = 'sphinx_rtd_theme'
```

### Provide documentation

Add **intro**,**mymodule** and **MyModule** on /doc/source/index.rst with **good indentation** like this

```rst
.. toctree::
    :maxdepth: 2
    :caption: Contents:


    intro
    code/mymodule
    code/MyModule
```

We want :
 - intro : simple file documentation
 - mymodule : describe the module
 - MyModule : describe the Class

We create this tree files :
 - ./doc/source/intro.rst
 - ./doc/source/code/mymodule.rst
 - ./doc/source/code/MyModule.rst


- **_static/** containt static file like ( Ex: static file for the html version), you can:
    - add image in this directory to use it in the doc
    - overload the theme by, for example, adding your **css/theme.css**

- **_templates/** containt temples file like ( Ex: template file for the html version), you can:
    - overload the theme by, for example, adding your **footer.html**