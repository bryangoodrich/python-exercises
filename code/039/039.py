# Title: List Out Of Lambda [in Python]
#
# An adaptation of Steve Losh's JavaScript exploration[1] with a hat tip to
# Hadley Wickham's Advanced R Programming[2] that led me there.
#
# References
# [1] http://stevelosh.com/blog/2013/03/list-out-of-lambda/
# [2] http://adv-r.had.co.nz/

empty_list = None # constant NULL function
 
def prepend(element, lst):
    def selector(x):
        return element if x == "head" else lst
    return selector

head = lambda x: x("head")
tail = lambda x: x("tail")
is_empty = lambda x: x is None

# [Alice, Bobby, Charlie]
ppl = prepend("Alice", prepend("Bobby", prepend("Charlie", empty_list)))
is_empty(empty_list)  # True
is_empty(ppl)         # False
head(ppl)             # Alice := ppl[0]
head(tail(ppl))       # Bobby := ppl[1]
head(tail(tail(ppl))) # Charlie := ppl[0]

def fmap(fn, lst):
    return empty_list if is_empty(lst) else prepend(fn(head(lst)), fmap(fn, tail(lst)))

# [2, 5, 7]
nums = prepend(2, prepend(5, prepend(7, empty_list)))
sq = fmap(lambda x: x*x, nums)
head(sq), head(tail(sq)), head(tail(tail(sq)))
# (4, 25, 49)
