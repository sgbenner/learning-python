def add(*args):
    total = 0
    for n in args:
        total += n

    return total


def calculate(**kwargs):
    print(kwargs)

calculate(add=123, multiply=500)

dict = {
    "add": 1,
    "add": 2,
    "add": 3
}

print(dict)
