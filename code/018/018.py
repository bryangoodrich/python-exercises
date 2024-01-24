class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if self.value is None:
            return self
        else:
            return func(self.value)

    def __rshift__(self, func):
        return self.bind(func)

    def __repr__(self):
        return f'Maybe({self.value})'

def add_one(value: any) -> Maybe:
    return Maybe(value + 1)

def multiply_by_two(value: any) -> Maybe:
    return Maybe(value * 2)

def square(value: any) -> Maybe:
    return Maybe(value * value)

square(multiply_by_two(add_one(Maybe(3))))
Maybe(3) >> add_one >> multiply_by_two >> square
# Maybe(64)

Maybe(None) >> add_one >> multiply_by_two >> square
# Maybe(None)
