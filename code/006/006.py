def use_state(initial_state):
    state = initial_state

    def set_state(new_state):
        nonlocal state
        state["value"] = new_state

    return state, set_state

count, set_count = use_state({"value": 0})
print(count["value"])  # Output: 0

increment = lambda: set_count(count["value"] + 1)
decrement = lambda: set_count(count["value"] - 1)

increment()  # 1
increment()  # 2
decrement()  # 1

print(count["value"])
# 1
