def is_expression_true(input_str):
    numbers = [int(x) for x in input_str.split(', ')]
    return all(x == int(x**0.5)**2 for x in numbers)
