import time
from functools import wraps
import logging

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

@timethis
def add(a, b):
    return a+b

countdown(10000)
print(add(2, 3))
# countdown = timethis(countdown)

# remove decorator
add_no_decorator = add.__wrapped__
print(add_no_decorator(2, 3))


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG, name='test')
def new_add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(new_add(3, 3))