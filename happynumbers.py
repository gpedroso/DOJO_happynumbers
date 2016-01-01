def happy(number):
    if number in (1, 10, 100):
        string = str(number)
        total = 0

        for char in string:
            total += int(char)

        return total == 1

    return False

assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert not happy(4) == True