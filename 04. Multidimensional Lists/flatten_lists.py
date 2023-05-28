initial_matrix = [el for el in input().split("|")]

new_list = []

for sub_string in initial_matrix[::-1]:
    new_list.extend(sub_string.split())

print(*new_list)
