# Usage
#
# python 0068.py Bryan
# Hello, Bryan!

def main(name):
    """ My main hook into my script or module """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        main("World")
        sys.exit(0)
    
    arg = sys.argv[1]
    main(arg)
