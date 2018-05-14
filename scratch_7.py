'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
6th prime is 13.

What is the 10 001st prime number?

'''


import math


def check_if_prime(h_factor):
    for y in range(2, round(math.sqrt(h_factor))+1):
        if h_factor % y == 0:
            return False
    return True


def create_prime_list(max_number):
    index = 3
    primes = []
    num_of_primes = 1
    while num_of_primes < max_number:
        print(index)
        if check_if_prime(index):
            primes.append(index)
            num_of_primes += 1
            print(num_of_primes)
        index += 2
    return primes


k = 10001
plist = create_prime_list(k)
print(max(plist))
print(104743)



