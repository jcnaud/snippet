# Atom

## Parameter
Settings->Editor->(Enable)Show Indet Guide

## Packages for general coding
- minimap
- atom-ide-ui
- symbols-tree-view : "CTRL+ALT+o"
- atom-ctags:
- git-log : "git log show"
- atom-scale-factor: multi zomm on multi open atom

## Packages for Python
- ide-python
- python-debugger

**Issue** with python-language-server (aka pyls).
**Solved** by downgrade pyls.
```bash
pip freeze
pip unisntall python-language-server
pip install python-language-server==0.19.0
```

## Packages to test:
- rst-preview-pandoc
