#!/usr/bin/bash
jupyter nbconvert --to markdown README.ipynb
python setup.py sdist
twine upload dist/*
