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

def my_avg(*args):
    pass

def my_car_desc(**kwargs):
    pass

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