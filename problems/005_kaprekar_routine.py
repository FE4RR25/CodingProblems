"""
Problem 005 — Kaprekar Routine

Take any 4-digit number that has at least two different digits.
For each step:
1. Rearrange its digits from largest to smallest.
2. Rearrange its digits from smallest to largest.
3. Subtract the smaller number from the larger one.
4. Repeat.

Example with 3524:
5432 - 2345 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Once you reach 6174, repeating the process keeps giving 6174.

Your task: write a program that prints the full sequence and the number of steps needed to reach 6174.
Important detail: numbers like 3087 can produce something like 0378, so you need to preserve leading zeros when rearranging digits.
"""

def create_numbers(number):
    lth = ""
    htl = ""
    for digit in sorted(number):
        lth = lth + digit
    for digit in sorted(number, reverse = True):
        htl = htl + digit
    return lth, htl

def subtract(htl, lth):
    new = int(htl)-int(lth)
    return str(new)

def add_zeros(num):
    while len(num) < 4:
        num = "0" + num
        print(f"added zero: {num}")
    return num


number = input("Input a Number >")
steps = 0

while True:
    if number == "6174":
        break

    number = add_zeros(number)

    if len(set(number)) == 1:
        break

    step += 1
    lth, htl = create_numbers(number)
    number = subtract(htl, lth)
    print(f"{htl} - {lth} = {number}")

print(f"Steps: {steps}")