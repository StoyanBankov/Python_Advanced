def even_odd_filter(**kwargs):

    if "even" in kwargs:
        kwargs["even"] = [el for el in kwargs["even"] if el % 2 == 0]

    if "odd" in kwargs:
        kwargs["odd"] = [el for el in kwargs["odd"] if el % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
