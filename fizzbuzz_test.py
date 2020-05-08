# pylint: disable=unused-variable
"""Unit tests for FizzBuzz"""

# import the code to be tested
from fizzbuzz import fizz, buzz, fibu, play

# import
from pytest import raises

def describe_a_fizzbuzz_program_that():
    """A program to play the FizzBuzz game"""

    def has_a_smoke_test():
        """Make sure our test infrastructure is working"""
        assert True == True

    def describes_a_fizz_function_that():

        def throws_an_error_if_fizz_has_no_input():
            """Make sure fizz() throws an error if there is no input"""
        with raises(Exception) as err_info:
            fizz() # pylint: disable=no-value-for-parameter
        assert err_info.type == TypeError
        assert 'missing 1 required positional argument' in str(err_info.value)


        def outputs_fizz_if_an_input_is_numeric_and_a_multiple_of_3():
            """checks to see if a number is a multiple of 3"""
        assert fizz(3) == 'Fizz'   # multiple of three
        assert fizz(4) == 4  # a non-multiple of three
        assert fizz(0) == 'Fizz'   # zero
        assert fizz(15) == 'Fizz'  # multiple of three and five
        assert fizz(-3) == 'Fizz'  # negative multiple of three
        assert fizz(-2) == -2 # negative non-multiple of three
        assert fizz(3.5) == 3.5  # non-integer
        assert fizz('Buzz') == 'Buzz'  # non-numeric
        assert fizz() == False  # no input
    def describes_a_buzz_function_that():
        def throws_an_error_if_buzz_has_no_input():
            """Make sure buzz() throws an error if there is no input"""
        with raises(Exception) as err_info:
            buzz() # pylint: disable=no-value-for-parameter
        assert err_info.type == TypeError
        assert 'missing 1 required positional argument' in str(err_info.value)


        def outputs_buzz_if_an_input_is_numeric_and_a_multiple_of_5():
        """
        Checks to see if the input 'x' is a multiple of 5
        """
        assert buzz(3) == 'Buzz'   # multiple of three
        assert buzz(4) == 4  # a non-multiple of three
        assert buzz(0) == 'Buzz'   # zero
        assert buzz(15) == 'Buzz'  # multiple of three and five
        assert buzz(-5) == 'Buzz'  # negative multiple of five
        assert buzz(-2) == -2 # negative non-multiple of five
        assert buzz(3.5) == 3.5  # non-integer
        assert buzz('buzz') == 'buzz'  # non-numeric
        assert buzz() == False  # no input

    def describes_a_fibu_function_that():
        def throws_an_error_if_fibu_has_no_input():
            """Make sure fizz() throws an error if there is no input"""
        with raises(Exception) as err_info:
            fibu() # pylint: disable=no-value-for-parameter
        assert err_info.type == TypeError
        assert 'missing 1 required positional argument' in str(err_info.value)

        def outputs_fizzbuzz_if_an_input_is_numeric_and_a_multiple_of_15():
        """checks to see if a number is a multiple of 15"""
        assert fizz(3) == 'Fizzbuzz'   # multiple of three
        assert fizz(4) == 4  # a non-multiple of three
        assert fizz(0) == 'Fizzbuzz'   # zero
        assert fizz(15) == 'Fizzbuzz'  # multiple of three and five
        assert fizz(-3) == 'Fizzbuzz'  # negative multiple of three
        assert fizz(-2) == -2 # negative non-multiple of three
        assert fizz(3.5) == 3.5  # non-integer
        assert fizz('fizz') == 'fizz'  # non-numeric
        assert fizz() == False  # no input

    def can_play_fizzbuzz():
        assert play(1,15) == [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizzbuzz'
        ]