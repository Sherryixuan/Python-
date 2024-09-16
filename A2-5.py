import sys
def largest_contiguous_interval(n, test_cases):
    results = []
    for line in test_cases:
        numbers = list(map(int, line.split()))
        intervals = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
        
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        max_length = 0
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                max_length = max(max_length, current_end - current_start)
                current_start = start
                current_end = end

        max_length = max(max_length, current_end - current_start)
        results.append(max_length)
    
    return results
input_data = sys.stdin.read().strip().split('\n')
#input_data = '''4
#1 3 0 2 3 4 
#0 3 1 2 1 3 4 4
#0 2 3 4 5 6 3 6 2 4
#1 1 1 2 1 3 1 4 1 5'''.strip().split("\n")
n = input_data[0]
test_cases = input_data[1:]

# Output
results = largest_contiguous_interval(n, test_cases)
for result in results[0:int(n)]:
    print(result)
