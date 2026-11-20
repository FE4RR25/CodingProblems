"""
Problem 006 — Perfect Numbers

A perfect number is a positive integer that equals the sum of its proper divisors
(all positive divisors excluding the number itself).

For example, 6 is a perfect number because:
1+2+3=6

Another example is 28:
1+2+4+7+14=28

Your task. Write a Python program that:
1. Takes a positive integer n as input.
2. Finds all perfect numbers between 1 and n.
3. Prints the perfect numbers it finds.

Example output:
Input a number: 1000
Perfect numbers: [6, 28, 496]
"""

def create_divisors(x):
    divisors = []
    for n in range(1, x, 1):
        if x % n == 0:
            divisors.append(n)
    return divisors

while True:
    n = int(input("Input a Number > "))
    perfect_numbers = []

    for x in range(1, n+1, 1):
        divisors = create_divisors(x)
        total = sum(divisors)

        if x == total:
            perfect_numbers.append(x)

    print(f"Perfect Numbers: {perfect_numbers}")

