"""
Top-Level Example Module

This module is at the root of the Packit package. It can be
imported like the following

`import packit.topmod as mod`
`from packit import topmod as mod`

Then you can use content from topmod via `mod.add` and such.
"""

print("Loading module topmod from package Packit ...")

TOPMODFLAG = 1

def add(x, y):
    """ Adds two values x and y """
    print("Calling add from module topmod in package Packit ...")
    return x+y
