def concatenate(*args, **kwargs):

    result = ""

    for el in args:
        result += el

    for key in kwargs.keys():
        if key in result:
            result = result.replace(key, kwargs[key])

    return result
