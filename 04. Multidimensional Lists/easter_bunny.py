size = int(input())

matrix = [list(input().split()) for _ in range(size)]

positions = ("up", "down", "left", "right")
bunny_found = False

while not bunny_found:
    for row in range(size):
        for col in range(size):
            collected_eggs = 0
            current_position = ""
            best_location = []

            if matrix[row][col] == "B":
                bunny_found = True

                for position in positions:
                    current_eggs = 0
                    current_location = []

                    if position == "up":
                        if row > 0:
                            for step in range(row-1,-1,-1):
                                if matrix[step][col] != "X":
                                   current_eggs += int(matrix[step][col])
                                   current_location.append([step, col])
                                else:
                                    break

                    elif position == "down":
                        if row < size-1:
                            for step in range(row+1, size):
                                if matrix[step][col] != "X":
                                   current_eggs += int(matrix[step][col])
                                   current_location.append([step, col])
                                else:
                                    break

                    elif position == "left":
                        if col > 0:

                            for step in range(col-1,-1,-1):
                                if matrix[row][step] != "X":
                                   current_eggs += int(matrix[row][step])
                                   current_location.append([row, step])
                                else:
                                    break

                    elif position == "right":
                        if col < size-1:

                            for step in range(col+1, size):
                                if matrix[row][step] != "X":
                                   current_eggs += int(matrix[row][step])
                                   current_location.append([row, step])
                                else:
                                    break

                    if collected_eggs <= current_eggs:
                        collected_eggs = current_eggs
                        current_position = position
                        best_location = current_location

                print(current_position)
                for el in best_location:
                    print(el)

                print(collected_eggs)
