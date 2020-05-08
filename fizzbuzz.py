""" a fizzbuzz program"""

# import necessary supporting libraries
from numbers import Number

def fizz(x):
    """
    Checks to see if the input is numeric and a multiple of three.
    If it is, it outputs 'Fizz'.
    Otherwise, it outputs the input.
    """
    
    return 'Fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
    """
    Checks to see if the input is numeric and a multiple of five.
    If it is, it outputs 'Buzz'.
    Otherwise, it outputs the input.
    """
    
    return 'Buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fibu(x):
    """
    Checks to see if the input is numeric and a multiple of fifteen.
    If it is, it outputs 'FizzBuzz'.
    Otherwise, it outputs the input.
    """
    
    return 'FizzBuzz' if isinstance(x, Number) and x % 15 == 0 else x

    #if isinstance(x, Number) and x % 3 == 0:
        #return 'fizz'
    #else:
        #return x
def play(start, end):
    """
        Given a start number and an end number, play FizzBuzz
        starting at 'start' and ending at 'end' and output the
        results as a list (array).
    """
    # initialize an empty collection to hold our output
    output = []
    # loop through the numbers from start to end
    for x in range(start, end + 1):
        output.append(buzz(fizz(fibu(x))))
    # return the output
    return output
