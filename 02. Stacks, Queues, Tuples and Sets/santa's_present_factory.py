from collections import deque

materials = deque([int(el) for el in input().split()])
level = deque([int(el) for el in input().split()])

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
current_presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and level:

    current_material = materials.pop()
    current_level = level.popleft()

    if current_material == 0 and current_level == 0:
        continue

    elif current_material == 0:
        level.appendleft(current_level)
        continue

    elif current_level == 0:
        materials.append(current_material)
        continue

    total_magic_level = current_material * current_level

    if total_magic_level in presents:
        present = presents[total_magic_level]
        current_presents[present] += 1

    elif total_magic_level < 0:
        materials.append(current_material+current_level)

    else:
        materials.append(current_material+15)

if (current_presents["Doll"] >= 1 and current_presents["Wooden train"] >= 1)\
        or (current_presents["Teddy bear"] >= 1 and current_presents["Bicycle"] >= 1):
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(materials[material]) for material in range(len(materials)-1, -1, -1)])}")

if level:
    print(f"Magic left: {', '.join([str(magic) for magic in level])}")

for key, value in sorted(current_presents.items()):
    if value > 0:
        print(f"{key}: {value}")
