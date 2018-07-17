"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def main():
    cap = 600851475143
    max_divisor = 1
    while cap > 1:
        for i in range(2, int(cap) + 1):
            if cap % i == 0:
                cap /= i
                if i > max_divisor:
                    max_divisor = i
                break
    print(max_divisor)



if __name__ == "__main__":
    main()