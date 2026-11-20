"""
Problem 003 — Happy Numbers

A positive integer is called happy if repeatedly replacing the number with the sum of the squares of its digits eventually reaches 1.

Example with 19:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
So 19 is a happy number.

Your task: write a program that takes a number and determines whether it is happy or not.
The catch: some numbers never reach 1; they fall into a loop. Your program therefore needs a way to detect when it has seen the same number before."""


def check(number, visited_numbers):
    if number in visited_numbers:
        return True
    else:
        return False

def calculate_squares(number):
    new = 0
    for digit in str(number):
        new += int(digit)**2
    return new


while True:
    number = int(input("Input a Number: "))
    og = number
    visited = set()

    while check(number, visited) == False:
        if number == 1:
            print(f"{og} is a Happy Number!\n")
            break
        visited.add(number)
        number = calculate_squares(number)

    if check(number,visited):
        print(f"{og} is not a Happy Number!")



    






# Get number
# calculate new number
# check if new number was already calculated or is 1
# if not calculate new number