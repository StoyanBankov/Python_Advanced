from collections import deque

quantity = int(input())
orders = list(map(int, input().split()))

orders_queue = deque()

print(max(orders))

while orders:
    orders_queue.append(orders.pop(0))

while orders_queue:
    current_order = orders_queue[0]

    if quantity < current_order:
        break

    else:
        quantity -= current_order
        orders_queue.popleft()

if len(orders_queue) == 0:
    print("Orders complete")

else:
    print(f"Orders left: {' '.join([str(el) for el in orders_queue])}")
