prices = ["$120", "$340", "$50", "$90"]

result = list(map(
      lambda num: num[1:], prices
))

print(result)