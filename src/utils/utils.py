import functools
import time
from typing import Callable

from loguru import logger


# Print the run time of the decorated function.
def timer(func: Callable) -> Callable:
    """Display the execution time of the decorated function.

    Args:
        func(function): Function to be decorated and showing the runtime.

    Returns:
        timer_wrapper(Callabe): Run and Logging the runtime of the input <func>.
    """
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        logger.info(f"{func.__name__!r} finished in {run_time:.4f} secs.")

        return value

    return timer_wrapper

# Analyze the function behaviour in details
def debug(func: Callable) -> Callable:
    """Display the input <func> signature and return the output value.

    Args:
        func(Callabe): Function to be decorated and showing the runtime.


    Returns:
        debug_wrapper(Callabe): Run and Logging the signature and the value of the input <func>.
    """
    @functools.wraps(func)
    def debug_wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        # Construct the function signature string
        signature = ", ".join(args_repr + kwargs_repr)
        value = func(*args, **kwargs)
        log_message = f"Calling -> {func.__name__}({signature}), Returns -> {value!r}"
        logger.info(log_message)

        return value

    return debug_wrapper

# Sleep 1 second before calling the function
def slow_down(func: Callable) -> Callable:
    """Sleep 1 second before calling the input <func>

    Args:
        func(Callabe): Function to be decorated and showing the runtime.


    Returns:
        slow_down_wrapper(Callabe): Sleep 1 second before calling the input <func>.
    """
    @functools.wraps(func)
    def slow_down_wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return slow_down_wrapper


if __name__ == "__main__":

    # Test timer decorator
    @timer
    def waste_some_time(num_times=10):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])

    waste_some_time()

    # Test debug decorator
    @debug
    def make_message(param0='test', param1=None):
        return f"param0:{param0}, param1:{param1}"

    make_message()

    # Test slow_down decorator
    @slow_down
    def countdown(num=3):
        if num == 0:
            print("Liftoff!")
        else:
            print(num)
            countdown(num - 1)

    countdown(3)
