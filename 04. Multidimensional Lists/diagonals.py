rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

sum_primary = 0
sum_secondary = 0

primary = []
secondary = []

for row_index in range(rows):
    sum_primary += matrix[row_index][row_index]
    primary.append(matrix[row_index][row_index])

    for _ in range(len(matrix[row_index])):
        sub_list = list(reversed(matrix[row_index]))
        sum_secondary += sub_list[row_index]
        secondary.append(sub_list[row_index])
        break

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum_secondary}")
