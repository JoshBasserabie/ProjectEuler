"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main():
    answer = 1
    for i in range (1, 21):
        answer = lcm(answer, i)
    print(int(answer))

def lcm(a, b):
    return a * b / gcd(a, b)

def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(a, b % a)

if __name__ == "__main__":
    main()