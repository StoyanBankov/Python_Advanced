from collections import deque

number_of_pumps = int(input())

current_pump = deque()

for _ in range(number_of_pumps):
    pumps = list(map(int, input().split()))
    current_pump.append(pumps)

for i in range(number_of_pumps):
    fuel = 0
    is_valid = True

    for el in range(number_of_pumps):
        current = current_pump.popleft()
        fuel += current[0]
        fuel -= current[1]

        if fuel < 0:
            is_valid = False

        current_pump.append(current)

    if is_valid:
        print(i)
        break

    current_pump.append(current_pump.popleft())
