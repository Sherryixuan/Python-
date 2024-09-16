import sys
def max_non_overlapping_intervals(n, test_cases):
    results = []
    for line in test_cases:
        numbers = list(map(int, line.split()))
        intervals = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = float('-inf')
        for start, end in intervals:
            if start > last_end:
                last_end = end
                count += 1
        results.append(count)
    
    return results

input_data = sys.stdin.read().strip().split('\n')
n = input_data[0]
test_cases = input_data[1:]

# Output
results = max_non_overlapping_intervals(n, test_cases)
for result in results[0:int(n)]:
    print(result)
