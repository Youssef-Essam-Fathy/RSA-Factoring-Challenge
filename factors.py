#!/usr/bin/python3
import math

def factorize(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return i, num // i;
    return num, 1 # if num is prime number

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factor1, factor2 = factorize(number)
            print(f"{number}={factor1}*{factor2}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])
