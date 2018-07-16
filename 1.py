"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    sum = 0.0
    # Add multiples of 3
    sum += 3 * 334 / 2 * 333
    # Add multiples of 5
    sum += 5 * 200 / 2 * 199
    # Subtract multiples of 15, which have been counted twice
    sum -= 15 * 67 / 2 * 66
    print(sum)

if __name__ == "__main__":
    main()