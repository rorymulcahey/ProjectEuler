'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1
to 20?

'''

import math


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


def create_prime_list(max_number):
    num_list = []
    for x in range(1, max_number + 1):
        num_list.append(x)
    primes = []
    for x in range(1, len(num_list)):
        if check_if_prime(num_list[x]):
            primes.append(num_list[x])
    return primes


def find_min_number(highest_factor, primes):
    a = []
    number = 1
    for i in range(0, len(primes)):
        a.append(1)
        if primes[i] <= math.sqrt(highest_factor):
            a[i] = (math.floor(math.log(k) / math.log(primes[i])))
        number = number * primes[i] ** a[i]
    return number


print(19*17*13*11*7*5*3*3*2*2*2*2)

k = 20
plist = create_prime_list(k)
num = find_min_number(k, plist)
print(num)



