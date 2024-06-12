def foo():
    pass

def first_function():
    print('Hello from first_function().')


def positional_f(name, age):
    print(name + ' is ' + str(age) + ' years old.')


def keword_f(name, age):
    print(name + ' is ' + str(age) + ' years old.')

def default_f(degrees, measure = 'Fahrenheit'):
    print('Temperature today is ' + str(degrees) + ' degrees ' + measure)

def avg_2(a: int, b: int) -> float:
    return (a + b) / 2

def avg_3(a, b, c):
    return (a + b + c) / 3
def my_avg(*args):
    average = sum(args) / len(args)
    return average, args[0]

def my_car_desc(**kwargs):
    if "model" in kwargs.keys():
        print(kwargs.get("model"))

    if "make" in kwargs.keys():
        print(kwargs.get("make"))



def iter(sz):
    """
    yield example
    :param sz:
    :return:
    """
    for i in range(sz):
        yield i

def func(lst):
    """
    By ref side effect
    :param lst:
    :return:
    """
    lst.clear()