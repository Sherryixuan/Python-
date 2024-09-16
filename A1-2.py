import sys

lines = sys.stdin.read().strip().split('\n')
    
for line in lines:
    numbers = list(map(int, line.split()))
    if len(numbers) == 1 and numbers[0] == 0:
        break
        
    pair = {}
    found = False
    min_sum = 10**1000000
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            s = numbers[i] + numbers[j]
            if s in pair:
                if pair[s] != (numbers[i], numbers[j]) aand pair[s] != (numbers[j], numbers[i]):
                    found=True
                    min_sum = min(min_sum,s)
            else:
                pair[s] = (numbers[i], numbers[j])
    if found :
        print(f"yes: {min_sum}")
    else:
        print("None")



