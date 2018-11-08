def slash_join(*args):
    temp = list()
    for arg in args:
        if arg is None:
            continue
        if isinstance(arg, int):
            arg = str(arg)
        temp.append(arg.strip('/'))
    return '/'.join(temp)