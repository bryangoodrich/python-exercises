import time

def tictoc(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"Time to run {fn.__name__}: {end-start:.2f}")
        return result
    return wrapper

@tictoc
def throttle(n=5):
    time.sleep(n)
    print("Done!")
  
throttle()
# Done!
# Time to run throttle: 5.01

float(x=5)  # float(x=0, /)
# TypeError: float() takes no keyword arguments

# Position Only
def norm(x, y, z=None, /):
    s = x**2 + y**2 + (z**2 if z else 0)
    return s**(1/3) if z else s**(1/2)


pts = (3, 5), (3, 5, 7)
norm(*pts[0])  # 5.830951894845301
norm(*pts[1])  # 4.362070671454838


# Keyword Only + positional argument
def greetings(name, *, greeting="Hello"):
    return f"{greeting}, {name}"

greetings("Bob")
# 'Hello, Bob'

greetings("Bob", "Hi")
# TypeError: greetings() takes 1 positional argument but 2 were given

greetings("Bob", greeting="Hi")
# 'Hi, Bob'

def headline(text, /, border="-", *, width=50):
    return f" {text} ".center(width, border)

headline("Python")
# '--------------------- Python ---------------------'

headline("Python", "=")
# '===================== Python ====================='

headline("Python", border="+")
# '+++++++++++++++++++++ Python +++++++++++++++++++++'

headline("Python", "=", 30)  
# SyntaxError: positional argument follows keyword argument!

headline("Python", border="=", width=20)
'====== Python ======'
