def process_values(values, callback):
    for value in values:
        result = callback(value)
        print(f"Processed value: {result}")


def multiply(*numbers):
    x, y = numbers
    z = x*y
    return z

values = [1, 2, 3, 4, 5]

print(multiply(8,9))