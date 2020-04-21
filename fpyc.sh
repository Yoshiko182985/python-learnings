#!/bin/bash
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
echo "Deleted the effin' pyc files!"
