'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import math
# initial = 13195
# h_prime = 1
initial = 600851475143


def find_factor(number):
    current_prime = 1
    for x in range(1, round(math.sqrt(number))):
        if number % x == 0:
            if check_if_prime(x):
                current_prime = x
    return current_prime


def check_if_prime(h_factor):
    for y in range(2, h_factor):
        if h_factor % y == 0:
            return False
    return True


h_prime = find_factor(initial)
print(h_prime)


