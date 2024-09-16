import sys
import math




def gcd_of_list(numbers):
    gcd_result = numbers[0]
    for number in numbers[1:]:
        gcd_result = math.gcd(gcd_result, number)
    return gcd_result

def main():
    lines = sys.stdin.read().strip().split('\n')
    
    for line in lines:
        numbers = list(map(int, line.split()))
        if len(numbers) == 1 and numbers[0] == 0:
            break
        gcd_result = gcd_of_list(numbers)
        print(f"The gcd of the integers is {gcd_result}.")

main()
