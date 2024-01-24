def sum_total(id):
    data = [0]
    def update(value):
        data[0] += value
        print(f"client {id} contains {data[0]}")
    
    return update

def last_three(id):
    data = []
    def update(value):
        data.append(value)
        if len(data) > 3:
            data.pop(0)
        print(f"client {id} contains {data}")
    
    return update

def show_now(id):
    data = [0]
    def update(value):
        data[0] = value
        print(f"client {id} contains {data[0]}")
    
    return update

def observable(initial_subscribers = []):
    subscribers = initial_subscribers
    
    def register(subscriber):
        subscribers.append(subscriber)
    
    def unregister(subscriber):
        subscribers.remove(subscriber)
    
    def update(value):
        for subscriber in subscribers:
            subscriber(value)
    
    return update, register, unregister

client1 = sum_total("Albert")
client2 = last_three("Barry")
client3 = show_now("Chris")

update_subs, register_subs, unregister_subs = observable([client1, client2])
update_subs(5)
# client Albert contains 5
# client Barry contains [5]
register_subs(client3)
update_subs(10)
# client Albert contains 15
# client Barry contains [5, 10]
# client Chris contains 10
update_subs(15)
# client Albert contains 30
# client Barry contains [5, 10, 15]
# client Chris contains 15
unregister_subs(client3)
update_subs(30)
# client Albert contains 60
# client Barry contains [10, 15, 30]
