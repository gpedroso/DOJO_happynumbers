def sum_of_squares(number):
    string = str(number)
    digits = [int(char)**2 for char in string]
    total = sum(digits)
    return total

def happy(number):
    box = []
    n = number
    while n!=1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1


assert sum_of_squares(130) == 10
assert happy(1) == True
assert happy(10) == True
assert happy(100) == True
assert happy(130) == True
assert happy(97) == True
assert not happy(4) == True