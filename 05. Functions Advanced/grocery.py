def grocery_store(**kwargs):

    result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return '\n'.join([f"{key}: {value}" for key, value in result])
