import sys
lines = sys.stdin.read().split("\n")
for line in lines:
    for i in range(0,len(line), 2):
        print(line[i], end = '')
    print()
        
