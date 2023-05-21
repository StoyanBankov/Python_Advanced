clothes = list(map(int, input().split()))
capacity = int(input())

current_sum = 0
used_racks = 1

while clothes:

    if 0 <= clothes[-1] <= 20:
        if 0 <= capacity <= 20:

            if clothes[-1] + current_sum < capacity:
                current_sum += clothes.pop()

            elif clothes[-1] + current_sum == capacity:
                if len(clothes) > 1:
                    clothes.pop()
                    current_sum = 0
                    used_racks += 1
                else:
                    break

            else:
                used_racks += 1
                current_sum = 0

        else:
            exit()

    else:
        clothes.pop()

print(used_racks)
