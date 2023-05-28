rows = int(input())

matrix = [[int(sub_list) for sub_list in input().split()] for _ in range(rows)]

command = input()

while command != "END":
    split_command = command.split()
    current_command = split_command[0]

    row = int(split_command[1])
    col = int(split_command[2])
    value = int(split_command[3])

    if 0 <= row < rows and 0 <= col < rows:
        if current_command == "Add":
            matrix[row][col] += value

        elif current_command == "Subtract":
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    command = input()

for el in matrix:
    print(*el)
