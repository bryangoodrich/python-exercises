"""
Subpack Example Sub-Package

This subpackage of Packit shows how we can nest content via
subfolders with their own __init__ scripts for import. 
Typically these subpackages help organize content by some
topic so common code of a certain type can be grouped together
from a single import. 

For instance, the `datatime` package has 
both a `date` and `datetime` subpackage that are used for date
and datetime operations, respectively.
"""

from packit.subpack.barn import Barn, Feed
from packit.subpack.farm import cow  # absolute import path
from .farm import sheep, dog         # relative import path

print("Loading subpackage subpack from package Packit ...")
