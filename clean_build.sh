#!/bin/bash

# Remove build directories
rm -rf build dist *.egg-info

# Rebuild the package
python -m build