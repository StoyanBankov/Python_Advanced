def even_odd(*args):
    command = args[-1]

    if command == "even":
        result = []
        for el in args[:-1]:
            if el % 2 == 0:
                result.append(el)

        return result

    elif command == "odd":
        result = []
        for el in args[:-1]:
            if el % 2 != 0:
                result.append(el)

        return result
