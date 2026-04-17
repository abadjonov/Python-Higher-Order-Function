sentence = "Functional programming in Python is very powerful and elegant"

top3_soz = sorted(sentence.split(),
                key=lambda soz: len(soz), 
                reverse=True)[:3]

print(top3_soz)