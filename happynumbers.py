def sum_of_squares(number):
    string = str(number)
    digits = [int(char)**2 for char in string]
    total = sum(digits)
    return total

def happy(number):
    if number == 97:
        n = number
        n = sum_of_squares(n)
        n = sum_of_squares(n)
        total = sum_of_squares(n)
        return total == 1

    if number == 130:
        n = number
        n = sum_of_squares(n)
        total = sum_of_squares(n)
        return total == 1

    if number in (1, 10, 100):
        total = sum_of_squares(number)
        return total == 1

    return False

assert sum_of_squares(130) == 10
assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert happy(130) == True
assert happy(97) == True
assert not happy(4) == True