def difference(*args):
    if not args:
        return 0
    minimum = args[0]
    maximum = args[0]
    for num in args:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num     
    result = maximum - minimum
    return round(result, 2)
