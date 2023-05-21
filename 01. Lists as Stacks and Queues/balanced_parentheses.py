expression = input()

symbols = []

curly = "{}"
square = "[]"
regular = "()"

is_balanced = True

for el in range(len(expression)):
    if len(symbols) > 0:
        if symbols[-1]+expression[el] == curly or symbols[-1]+expression[el] == square or\
                symbols[-1]+expression[el] == regular:
            symbols.pop()
            is_balanced = True

        else:
            symbols.append(expression[el])
            is_balanced = False
    else:
        symbols.append(expression[el])

if is_balanced and len(symbols) == 0:
    print("YES")
else:
    print("NO")
