import random

foo = random.randint(1, 10)
is_even = foo % 2 == 0

if is_even:
    bar = "Go Left"
else:
    bar = "Go Right"

foobar = "GO LEFT" if is_even else "GO RIGHT"
print(f"foo is {foo} so {bar}. I said {foobar}!")
# foo is 4 so Go Left. I said GO LEFT!