import sys
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
        


lines = sys.stdin.read().split()
player = [float(i) for i in lines[2::2]]

quick_sort(player, 0, len(player) - 1);
    
score = 0
for m in range(int(lines[0])):
    prob = player[m]
    score += (m + 1) * prob
print("{:.3f}".format(score))

