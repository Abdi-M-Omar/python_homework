# --------------------------------------------------
# Task 2: A Decorator that Takes an Argument
# --------------------------------------------------


# A decorator factory.
# It accepts a type (such as str, int, or float)
# and returns a decorator.
def type_converter(type_of_output):

    # This decorator receives the function to decorate.
    def decorator(func):

        # Wrapper accepts any positional and keyword arguments.
        def wrapper(*args, **kwargs):

            # Call the original function.
            x = func(*args, **kwargs)

            # Convert the return value to the requested type.
            return type_of_output(x)

        return wrapper

    return decorator


# --------------------------------------------------
# Function 1
# Returns the integer 5.
# The decorator converts the result to a string.
# --------------------------------------------------
@type_converter(str)
def return_int():
    return 5


# --------------------------------------------------
# Function 2
# Returns a string that cannot be converted to an int.
# The decorator will raise a ValueError.
# --------------------------------------------------
@type_converter(int)
def return_string():
    return "not a number"


# --------------------------------------------------
# Main Program
# --------------------------------------------------

# The returned value should now be a string.
y = return_int()
print(type(y).__name__)      # Expected output: str

# Attempt to convert "not a number" to an integer.
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")