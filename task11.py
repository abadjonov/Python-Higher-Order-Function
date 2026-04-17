nums = list(range(1, 21))

juft = filter(
    lambda x: x % 2 == 0, nums
)

kvadrat = map(
   lambda kv: kv ** 2, juft
)

print(list(kvadrat))