"""
Problem 002 — Collatz Sequence

Given a positive integer n, repeatedly apply these rules:

* If n is even, divide it by 2.
* If n is odd, multiply it by 3 and add 1.
* Continue until you reach 1.

Your task: Write a program that takes n and outputs the complete sequence, 
the number of steps required to reach 1, and the largest number encountered
"""

def decide(number):

    if number % 2 == 0:
        new = number//2
    else:
        new = number * 3 + 1

    return new


def print_results(sequence, steps, maximum):

    print(f"Sequence: {sequence}")
    print(f"Steps: {steps}")
    print(f"Max: {maximum}")

    return 


while True:
    sequence = []
    number = int(input("\nInput a Number to run the Sequence\n> "))

    while number > 1:
        sequence.append(number)
        number = decide(number)

    sequence.append(1)
    steps = len(sequence) - 1 
    maximum = max(sequence)

    print_results(sequence, steps, maximum)

    
