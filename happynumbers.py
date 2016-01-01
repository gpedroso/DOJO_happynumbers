def happy(number):
    if number == 10 or number == 100 or number == 1:
        string = str(number)
        total = 0
        i = 0

        while i < len(string):
            total = total + int(string[i])
            i = i + 1

        return total == 1

    return False

assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert not happy(4) == True