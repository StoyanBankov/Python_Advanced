number = int(input())

queries = []

for query in range(number):
    current_query = input()
    split_query = current_query.split()

    if len(current_query) > 1:
        number_to_push = int(split_query[1])
        queries.append(number_to_push)

    else:
        if len(queries) > 0:

            if split_query[0] == "2":
                queries.pop()

            elif split_query[0] == "3":
                print(max(queries))

            elif split_query[0] == "4":
                print(min(queries))

print(f"{', '.join([str(el) for el in reversed(queries)])}")
