text = input()

text_set = set()

count = {}

for el in text:
    text_set.add(el)

for el1 in text_set:
    count[el1] = text.count(el1)

for key, value in sorted(count.items()):
    print(f"{key}: {value} time/s")
