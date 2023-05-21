count = int(input())

unique = set()

for _ in range(count):
    current_line = set([el for el in input().split()])
    unique = unique | current_line

print(*unique, sep="\n")
