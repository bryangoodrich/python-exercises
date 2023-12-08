from packit.subpack import Barn, cow, dog, sheep

# No static method
animals = [cow, dog, sheep]
barn = Barn(10)  # This is pointless!
barn.fromlist(animals)

# With static method
barn = Barn.fromlist(animals)