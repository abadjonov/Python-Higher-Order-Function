numbers = [18, 29, 3, 45, 7, 12]

#birinchi usul
resultmax = max(
    numbers, key=lambda x: x
)
resultmin = min(
    numbers, key=lambda x: x
)


#ikkinchi usul
resultmax2 = max(numbers)
resultmin2 = min(numbers)

print(resultmax2, resultmin2)
print(resultmax, resultmin)