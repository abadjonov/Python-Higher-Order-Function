numbers = [4, -2, 0, 7, -9, 3, -1, 5]

result = filter(
    lambda x: x > 0,
    numbers
)

print(list(result))