def happy(number):
    if number < 10:
        return number in (1, 7)

    return (happy(sum([int(char)**2 for char in str(number)])))

assert all(happy(n) for n in (1,10,100,130,97))
assert not all (happy(n) for n in (2,3,4,5,6,8,9))