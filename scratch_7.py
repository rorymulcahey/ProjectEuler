'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
6th prime is 13.

What is the 10 001st prime number?

'''


def check_if_prime(h_factor):
    for y in range(2, h_factor):
        if h_factor % y == 0:
            return False
    return True


def create_prime_list(max_number):
    index = 2
    primes = []
    num_of_primes = 0
    while num_of_primes < max_number:
        print(index)
        if check_if_prime(index):
            primes.append(index)
            num_of_primes += 1
            print(num_of_primes)
        index += 1
    return primes


k = 10001
plist = create_prime_list(k)
print(max(plist))



