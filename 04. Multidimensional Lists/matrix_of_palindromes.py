rows, cols = [int(el) for el in input().split()]

matrix = [["" for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        matrix[row][col] = f"{chr(97 + row)}{chr(97 + col + row)}{chr(97 + row)}"

for el in matrix:
    print(*el)
