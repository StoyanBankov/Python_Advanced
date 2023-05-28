def age_assignment(*args, **kwargs):

    ages = {}

    for key, value in kwargs.items():
        for name in args:
            if name[0] == key:
                ages[name] = int(value)

    ages = sorted(ages.items(), key=lambda x: x[0])

    return '\n'.join([f"{el[0]} is {el[1]} years old." for el in ages])
