# packit
# ├── __init__.py
# ├── subpack
# │   ├── __init__.py
# │   ├── barn.py
# │   └── farm.py
# └── topmod.py
# 
# 1 directories, 5 files

import packit
# Loading module topmod from package Packit ...
# Loading package Packit ...

import packit
import packit.topmod as mod

print(mod.add(1,2))
# Calling add from module topmod in package Packit ...
# 3

print(packit.add(1, 2))
# Calling add from module topmod in package Packit ...
# 3

print(mod.TOPMODFLAG)
# 1

import packit.subpack as sub
# Loading subpackage subpack from package Packit ...

print(sub.cow)
# 'The cow goes moo'
print(sub.sheep)
# 'The sheep goes baa'

barn = sub.Barn(10, animals=['cow', 'sheep', 'dog'])
print(barn)
# Barn(3, 10)
