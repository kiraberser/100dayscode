#ulimeted Positional Arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3, 4, 5))

#Many keyword arguments **kwargs
#create a dictionary 

def calculate(**kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #    print(key)
    #    print(value)
    #n += kwargs["add"]
    #n *= kwargs["multiply"]
    #print(n)
calculate(add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        
my_car = Car(make="Nissan", model="GT")
print(my_car.model)
