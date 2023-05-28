def are_valid(row1, col1, row2, col2):
    if row1 <= rows-1 >= row2:
        return True

    if col1 <= cols-1 >= col2:
        return True


rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    sub_list = input().split()
    matrix.append(sub_list)

command = input()

while command != "END":
    split_command = command.split()

    if split_command[0] == "swap":
        if len(split_command[1:]) == 4:
            row1 = int(split_command[1])
            col1 = int(split_command[2])
            row2 = int(split_command[3])
            col2 = int(split_command[4])

            if are_valid(row1, col1, row2, col2):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for el in matrix:
                    print(*el)

            else:
                print("Invalid input!")

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()
