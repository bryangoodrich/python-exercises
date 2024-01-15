name = input("Enter a name: ")
part_of_body = input("Name a part of the body: ")
type_of_fluid = input("Pick a fluid: ")
a_substance = input("Name a substance: ")


story = f"""
-- Hall Pass --

{name} is sick with the {part_of_body} flu.

Drink more {type_of_fluid} and take {a_substance} as needed.
"""

print(story)
# -- Hall Pass --
# Bob is sick with the leg flu.
# Drink more orange juice and take mud as needed.