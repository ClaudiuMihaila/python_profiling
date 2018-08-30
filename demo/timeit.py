from functools import wraps
import time


def time_func(func):
    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        """a decorator which prints execution time of the decorated function"""
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s executed in %.4f seconds" % (func.__name__, (t2 - t1)))
        return result
    return timer_wrapper