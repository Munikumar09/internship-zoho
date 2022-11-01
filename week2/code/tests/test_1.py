# pylint: disable-all


def compare_two_numbers(num1: int, num2: int) -> bool:
    return num1 == num2


def max_of_two_numbers(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2


def test_compare_function_answer():
    assert compare_two_numbers(3, 3) == True
    assert compare_two_numbers(2, 4) == False
    assert compare_two_numbers(50, 40) == False


def test_max_function_answer():
    assert max_of_two_numbers(20, 10) == 20
    assert max_of_two_numbers(10, 10) == 10
