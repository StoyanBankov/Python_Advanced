rows, cols = [int(el) for el in input().split()]
snake = input()

matrix = [["" for _ in range(cols)] for _ in range(rows)]

counter = 0

for row in range(rows):
    for col in range(cols):
        matrix[row][col] = snake[col]
        snake += snake[col]

    counter += 1

    if counter == 2:
        matrix[row] = list(reversed(matrix[row]))
        counter = 0

    snake = snake[cols:]

for el in matrix:
    print(*el, sep="")
