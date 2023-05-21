from collections import deque

text = deque(color for color in input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}

secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}

result = []

while text:

    first_part = text.popleft()
    second_part = text.pop() if text else ""

    for word in (first_part+second_part, second_part+first_part):
        if word in all_colors:
            result.append(word)
            break

    else:
        for el in (first_part[:-1], second_part[:-1]):
            if el:
                text.insert(len(text)//2, el)

for current_color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[current_color].issubset(result):
        result.remove(current_color)

print(result)
