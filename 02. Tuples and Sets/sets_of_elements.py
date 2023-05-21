sequences = input().split()

n = int(sequences[0])
m = int(sequences[1])

n_set = set()
m_set = set()

for _ in range(n):
    current_n = int(input())
    n_set.add(current_n)

for _ in range(m):
    current_m = int(input())
    m_set.add(current_m)

print(*(n_set & m_set),sep="\n")
