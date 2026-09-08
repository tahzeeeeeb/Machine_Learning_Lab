def multiply(*args):
    result = 1
    for number in args:
        result = result * number
    return result

print(multiply(2, 3, 4))
print(multiply(5, 10))
print(multiply(1, 2, 3, 4, 5))
