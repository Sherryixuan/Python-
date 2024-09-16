import sys
def max_overlapping_intervals(n, test_cases):
    results = []
    for line in test_cases:
        numbers = list(map(int, line.split()))
        events = []
        for i in range(0, len(numbers), 2):
            start = numbers[i]
            end = numbers[i + 1]
            events.append((start, 'start'))
            events.append((end + 1, 'end'))

        events.sort(key=lambda x: (x[0], x[1] == 'start'))

        max_overlap = 0
        current_overlap = 0

        for event in events:
            if event[1] == 'start':
                current_overlap += 1
                max_overlap = max(max_overlap, current_overlap)
            else:
                current_overlap -= 1

        results.append(max_overlap)

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
results = max_overlapping_intervals(n, test_cases)
for result in results[0:int(n)]:
    print(result)
