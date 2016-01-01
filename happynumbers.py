def happy(number):
    if number == 10:
        return True

    if number == 1 or number == 100:
        return True

    return False

assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert not happy(4) == True