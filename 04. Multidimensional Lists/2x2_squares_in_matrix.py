rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    sub_list = input().split()
    matrix.append(sub_list)

matches = 0

for row in range(rows-1):
    for col in range(cols-1):
        current = matrix[row][col]
        next = matrix[row][col+1]
        below = matrix[row+1][col]
        diagonal = matrix[row+1][col+1]

        if current == next == below == diagonal:
            matches += 1

print(matches)
