size = int(input())

matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed = 0

while True:
    max_attacks = 0
    knight = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    current_row = row + position[0]
                    current_col = col + position[1]

                    if 0 <= current_row < size and 0 <= current_col < size:
                        if matrix[current_row][current_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight = [row, col]
                    max_attacks = attacks

    if knight:
        matrix[knight[0]][knight[1]] = "0"
        removed += 1

    else:
        break

print(removed)
