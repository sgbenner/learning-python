numbers = {
    0: {
        "a": "1",
        "b": "2"
    },
    1: 1
}

print(numbers[0]["b"])

def fibonacci(n):
    result = numbers.get(n)

    if result is None:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        numbers[n] = result

    return result
#
# print(fibonacci(600))
