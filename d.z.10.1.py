def custom_sequence_generator(start_value, func, n):
    current = start_value
    for _ in range(n):
        yield current
        current = func(current)
