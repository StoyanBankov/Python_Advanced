sequence = int(input())

names = set()

for name in range(sequence):
    current_name = input()
    names.add(current_name)

print(*names, sep="\n")
