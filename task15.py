votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

eng_kop_ovoz = max(votes, key=lambda x: x["votes"])

print(eng_kop_ovoz)