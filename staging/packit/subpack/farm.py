"""
Example Subpackage Module of Farm animals

Here we can predefine some statements of our farm animals.
"""

def sound(animal, noise):
    """ Defines a statement of animal going ... """
    return f"The {animal} goes {noise}"

cow = sound("cow", "moo")
dog = sound("dog", "woof")
sheep = sound("sheep", "baa")
