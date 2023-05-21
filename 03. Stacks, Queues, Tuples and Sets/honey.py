from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

total_honey = 0

while working_bees and nectar:

    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()

        if current_symbol == "/" and current_nectar == 0:
            continue
        else:
            honey_made = operations[current_symbol](current_bee, current_nectar)
            total_honey += abs(honey_made)

    else:
        working_bees.appendleft(current_bee)
        continue

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join([str(bee) for bee in working_bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(nec) for nec in nectar])}")
