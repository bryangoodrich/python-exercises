import packit
from packit import topmod as module
# Loading module topmod from package Packit ...
# Loading package Packit ...

print(f"Same! {packit.add(2,3)} == {module.add(2,3)}")
# Calling add from module topmod in package Packit ...
# Calling add from module topmod in package Packit ...
# Same! 5 == 5

print(f"Module only: flag == {module.TOPMODFLAG}")
# Module only: flag == 1

from packit import subpack as farm
# Loading subpackage subpack from package Packit ...

farm.dog
# 'The dog goes woof'

barn = farm.Barn(2)  # holds 2 animals, currently empty
barn.add(farm.cow)
barn.add(farm.sheep)
print(barn)
# Barn(2, 2)

barn.add(farm.dog)
# ValueError: cannot add animal, barn at capacity