"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

def main():
    numbers = [2]
    while len(numbers) < 10001:
        i = numbers[-1] + 1
        while is_composite(i):
            i += 1
        numbers.append(i)
    print(numbers[-1])

def is_composite(x):
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return True
    return False

if __name__ == '__main__':
    main()