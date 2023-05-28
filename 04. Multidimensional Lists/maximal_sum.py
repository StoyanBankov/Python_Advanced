rows, cols = [int(el) for el in input().split()]

matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = 0
current_max = []

for row in range(rows-2):
    for col in range(cols-2):
        one = matrix[row][col]
        two = matrix[row][col+1]
        tree = matrix[row][col+2]
        four = matrix[row+1][col]
        five = matrix[row+1][col+1]
        six = matrix[row+1][col+2]
        seven = matrix[row+2][col]
        eight = matrix[row+2][col+1]
        nine = matrix[row+2][col+2]

        total_sum = one + two + tree + four + five + six + seven + eight + nine

        if total_sum >= max_sum:
            max_sum = total_sum
            current_max.clear()
            current_max.append([one, two, tree])
            current_max.append([four, five, six])
            current_max.append([seven, eight, nine])

print(f"Sum = {max_sum}")

for el in current_max:
    print(*el)
