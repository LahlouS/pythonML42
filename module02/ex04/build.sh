#!/bin/sh

pip install --upgrade pip
pip install --upgrade setuptools
python -m pip install --upgrade build 
python -m build
pip install ./dist/my_minipack-0.0.1-py3-none-any.whl
# 