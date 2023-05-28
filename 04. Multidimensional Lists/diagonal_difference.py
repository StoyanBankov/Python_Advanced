size = int(input())

matrix = []

for _ in range(size):
    sub_list = list(map(int, input().split()))
    matrix.append(sub_list)

primary_sum = 0
secondary_sum = 0

for position in range(size):
    primary_sum += matrix[position][position]
    secondary_sum += matrix[position][size-position-1]

print(abs(primary_sum-secondary_sum))
