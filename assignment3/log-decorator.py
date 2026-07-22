# --------------------------------------------------
# Task 1: Writing and Testing a Decorator
# --------------------------------------------------

import logging


# Configure the logger to append records to decorator.log.
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# Log a function's name, arguments, keyword arguments,
# and returned value every time the function is called.
def logger_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional_parameters = list(args) if args else "none"
        keyword_parameters = kwargs if kwargs else "none"

        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(
            logging.INFO,
            f"positional parameters: {positional_parameters}"
        )
        logger.log(
            logging.INFO,
            f"keyword parameters: {keyword_parameters}"
        )
        logger.log(logging.INFO, f"return: {result}")

        return result

    return wrapper


# Takes no parameters and returns nothing.
@logger_decorator
def hello_world():
    print("Hello, World!")


# Takes any number of positional arguments and returns True.
@logger_decorator
def positional_function(*args):
    return True


# Takes any number of keyword arguments and returns logger_decorator.
@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator


# Call each decorated function.
hello_world()
positional_function(1, 2, 3)
keyword_function(name="Abdi", course="Python")

