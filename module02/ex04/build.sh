#!/bin/sh

pip install --update pip
pip install --upgrade setuptools
python -m pip install --upgrade build 
cd ./python_package && python -m build && cd ..

# 