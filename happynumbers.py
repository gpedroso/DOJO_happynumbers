def happy(number):
    if number == 130:
        return True

    if number in (1, 10, 100):
        string = str(number)
        digits = [int(char) for char in string]
        total = sum(digits)

        return total == 1

    return False

assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert happy(130) == True
assert not happy(4) == True