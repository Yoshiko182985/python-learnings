#!/bin/bash

#The purpose of this file is to delete all thos effin' pyc files and folders
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
echo "Deleted the effin' pyc files!"
