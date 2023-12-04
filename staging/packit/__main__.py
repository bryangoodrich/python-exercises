"""
Package Main Module

This double-under (dunder) module is automatically ran
when the package is executed like a module. This allows us
to conveniently encapsulate runtime behavior we want our 
package to support, whether that's as an API to using our
package for some purpose, for testing, or as a simple
script or demo.
"""

if __name__ == "__main__":
    print("Running Packit like a module ...")
    from packit import add
    print(f"using package adder: add(2, 3) = {add(2,3)}")
