def log(func):
    def wrapper(*args, **kw):
        print("call %s ()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("===10.3===")
    pass


if __name__ == "__main__":
    now()
