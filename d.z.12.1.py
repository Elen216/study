def prime_generator(limit):
    for number in range(2, limit + 1):
        is_prime = True 
        for i in range(2, number):
            if number % i == 0:
                is_prime = False  
                break  
        if is_prime:
            yield number
print(list(prime_generator(10)))
