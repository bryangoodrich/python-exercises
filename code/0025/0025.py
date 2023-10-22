# github.com/bryangoodrich/python-exercises
# code/0025/0025.py

class Writer:
    def __init__(self, value, log=None):
        self.value = value
        self.log = log if log else [("Start", value)]

    def bind(self, func):
        result = func(self.value)
        io = (self.value, result)
        return Writer(result, self.log + [io])

    __rshift__ = bind

    def __str__(self):
        return f"Writer({self.value})"

add_one = lambda x: x + 1
multiply_by_two = lambda x: 2 * x

result = Writer(5) >> add_one >> multiply_by_two
log = [f"{x[0]} -> {x[1]}" for x in result.log]

print(result)  # Access data via result.value
# Writer(12)

print(log)  # Log of pipeline "input -> output"
# ['Start -> 5', '5 -> 6', '6 -> 12']
