"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def main():
    MAX_PRIME = 2000000
    candidates = [True] * MAX_PRIME
    candidates[0], candidates[1] = False, False
    x = 2
    while x ** 2 < MAX_PRIME:
        i = x
        while i * x < MAX_PRIME:
            candidates[i * x] = False
            i += 1
        x += 1
        while not candidates[x]:
            x += 1
    primes = [p for p in range(MAX_PRIME) if candidates[p]]
    answer = sum(primes)
    print(answer)

if __name__ == "__main__":
    main()