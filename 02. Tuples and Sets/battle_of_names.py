sequence = int(input())

current_row = 1

odds_set = set()
evens_set = set()

for _ in range(sequence):
    name = input()

    sum_letters = sum([ord(letter) for letter in name]) // current_row

    if sum_letters % 2 == 0:
        evens_set.add(sum_letters)
    else:
        odds_set.add(sum_letters)

    current_row += 1

odds_sum = sum(odds_set)
evens_sum = sum(evens_set)

if odds_sum == evens_sum:
    print(*(odds_set | evens_set), sep=", ")

elif odds_sum > evens_sum:
    print(*(odds_set - evens_set), sep=", ")

elif evens_sum > odds_sum:
    print(*(odds_set ^ evens_set), sep=", ")
