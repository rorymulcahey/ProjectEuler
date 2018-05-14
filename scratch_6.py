'''

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.

'''


def sum_square_difference(num):
    total = 0
    square = 0
    for x in range(1, num + 1):
        total += x
        square += x**2
    total = total ** 2
    return total - square


print(sum_square_difference(100))
