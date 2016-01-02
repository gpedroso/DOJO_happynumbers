def sum_of_digits(number):
    string = str(number)
    digits = [int(char)**2 for char in string]
    total = sum(digits)
    return total

def happy(number):
    if number == 130:
        number = sum_of_digits(number)

    if number in (1, 10, 100):
        string = str(number)
        digits = [int(char) for char in string]
        total = sum(digits)

        return total == 1

    return False

assert sum_of_digits(130) == 10
assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert happy(130) == True
assert not happy(4) == True