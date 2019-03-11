from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}({}. {}) -> {}'
              .format(func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace
def fibonacci(n):
    """Return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


def main():
    help(fibonacci)


if __name__ == '__main__':
    main()