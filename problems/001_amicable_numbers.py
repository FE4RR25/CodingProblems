import numpy as np


def find_divisors(number):
    divisors = []
    for i in range(1, number, 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def calc_total(list):
    x = 0
    for i in list:
        x += i
    return x

while True:
    num1 = int(input("Input a number: "))
    div1 = find_divisors(num1)

    num2 = calc_total(div1)
    div2 = find_divisors(num2)

    num1_new = calc_total(div2)

    print(f"{num1} has divisors {div1}")
    print(f"{num2} has divisors {div2}")

    if num1_new == num1 and num1 != num2:
        print(f"{num1} and {num2} are an amicable pair")
