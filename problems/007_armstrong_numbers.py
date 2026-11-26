"""
Problem 007 — Armstrong Numbers

An Armstrong number is a positive integer that equals the sum of each of its digits raised to the power of the total number of digits.

For example, consider 153.
It has 3 digits, so: 1^3+5^3+3^3=153
Therefore, 153 is an Armstrong number.

Another example is 9474:
9^4+4^4+7^4+4^4=9474

Your task. Write a Python program that:
1. Takes a positive integer n as input.
2. Finds all Armstrong numbers between 1 and n.
3. Prints them in a list.

Example:
Input a Number > 500
Armstrong Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
"""
def check_if_armstrong(num):
    new = 0
    power = len(str(num))

    for digit in str(num):
        new += int(digit)**power
    if num == new:
        return True
  
    return False


while True:
    num = int(input("Check Number > "))
    armstrong_list = []

    for x in range(1, num+1, 1):
        print(f"Checking {x}")

        if check_if_armstrong(x):
            armstrong_list.append(x)


    print(f"Armstrong Numbers: {armstrong_list}")