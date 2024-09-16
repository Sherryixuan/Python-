import sys
def sum_of_intervals(n, test_cases):
    results = []
    index = 0
    for line in test_cases:
        numbers = line.split()
        total_length = 0
        for i in range(0,len(numbers), 2):
            start = int(numbers[i])
            end = int(numbers[i + 1])
            interval_length = end - start
            total_length += interval_length
        results.append(total_length)
    return results

# Input
#input_data = sys.stdin.read().strip().split('\n')
input_data = '''4
1 3 0 2 3 4
0 3 1 2 1 3 4 4
0 2 3 4 5 6 3 6 2 4
1 1 1 2 1 3 1 4 1 5'''.strip().split('\n')
n = input_data[0]
test_cases = input_data[1:]

# Output
results = sum_of_intervals(n, test_cases)
for result in results[0:int(n)]:
    print(result)
