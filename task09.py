names = ["Ali", "Valijon", "Sami", "Diyorbek"]

result = max(
    names, key=lambda eng_uzun: len(eng_uzun)
)

print(result)