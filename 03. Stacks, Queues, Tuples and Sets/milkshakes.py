from collections import deque

chocolate = list(map(int, input().split(", ")))
milk = list(map(int, input().split(", ")))

chocolate_deque = deque(chocolate)
milk_deque = deque(milk)

milkshakes = 0

while milkshakes != 5 and chocolate_deque and milk_deque:
    current_chocolate = chocolate_deque.pop()
    current_milk = milk_deque.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue

    elif current_chocolate <= 0:
        milk_deque.appendleft(current_milk)
        continue

    elif current_milk <= 0:
        chocolate_deque.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1

    else:
        milk_deque.append(current_milk)
        chocolate_deque.append(current_chocolate-5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_deque:
    print(f"Chocolate: {', '.join([str(el) for el in chocolate_deque])}")
else:
    print("Chocolate: empty")

if milk_deque:
    print(f"Milk: {', '.join([str(el1) for el1 in milk_deque])}")
else:
    print("Milk: empty")
