def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers_in_list(input_list):
    return [x for x in input_list if is_prime(x)]
