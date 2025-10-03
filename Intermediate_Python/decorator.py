import functools

def log(func):
    def wrapper(*args, **kw):
        print("call %s ()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    """
    The decorator is equal to
    now = log(now)
    """
    print("===10.3===")
    pass

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("{} {}()".format(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

        
@log('execute')
def now():
    '''
    Like recursive
    call log('execute')(now) --> call decorator(now) --> wrapper() --> print("execute now.__name__"); then call now()
    '''
    print('---10.3---')
    return 

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call {}()".format(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("---10.3---")
    return 

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("{} {}()".format(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    '''
    Like recursive
    call log('execute')(now) --> call decorator(now) --> wrapper() --> print("execute now.__name__"); then call now()
    '''
    print('---10.3---')
    return 

import time

def metric(func):
    print("{} executed in {} ms.".format(func.__name__, "?"))
    return func

@metric
def add(x,y):
    return x+y


if __name__ == "__main__":
    print(now.__name__)
    now()
    # add(3,5)
