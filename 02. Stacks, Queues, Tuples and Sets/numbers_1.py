first = set(map(int, input().split()))
second = set(map(int, input().split()))
sequence = int(input())

for _ in range(sequence):
    current_command = input().split()
    command = current_command[0]

    if command == "Add":
        sequence_to_add = current_command[1]
        numbers_to_add = current_command[2::]

        if sequence_to_add == "First":
            for n in numbers_to_add:
                first.add(int(n))

        elif sequence_to_add == "Second":
            for n1 in numbers_to_add:
                second.add(int(n1))

    elif command == "Remove":
        sequence_to_remove = current_command[1]
        numbers_to_remove = current_command[2::]

        if sequence_to_remove == "First":
            for n in numbers_to_remove:
                current_n = int(n)
                if current_n in first:
                    first.remove(current_n)

        elif sequence_to_remove == "Second":
            for n1 in numbers_to_remove:
                current_n1 = int(n1)
                if current_n1 in second:
                    second.remove(current_n1)

    elif command == "Check":
        if first.issubset(second) or second.issubset(first):
            print(True)
        else:
            print(False)

print(*(sorted(first)), sep=", ")
print(*(sorted(second)), sep=", ")
