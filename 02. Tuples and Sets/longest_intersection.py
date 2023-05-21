sequences = int(input())

intersections = {}

for el in range(sequences):
    current_sequence = input().split("-")
    first_sequence = current_sequence[0].split(",")
    second_sequence = current_sequence[1].split(",")

    first_start = int(first_sequence[0])
    first_end = int(first_sequence[1])

    second_start = int(second_sequence[0])
    second_end = int(second_sequence[1])

    first_set = set()
    second_set = set()

    for n1 in range(first_start, first_end +1):
        first_set.add(n1)

    for n2 in range(second_start, second_end +1):
        second_set.add(n2)

    intersections[el] = set(first_set & second_set)

lengths = set()
uniques = []

for value in intersections.values():
    if len(value) not in lengths:
        lengths.add(len(value))
        uniques.append(value)

max_len = max(lengths)

for el1 in uniques:
    if len(el1) == max_len:
        print(f"Longest intersection is {list(el1)} with length {max_len}")
