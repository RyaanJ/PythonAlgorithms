# Find largest possible value from adding k consecutive (side-by-side) elements in arr
arr = [5, 2, 10, 6, 3, 34, 8, 2]
k = 3
current_sum = 0
max_sum = 0
i = 0
j = k - 1

while i < j:
    for e in range(i, j + 1):
        current_sum += arr[e]
    max_sum = max(current_sum, max_sum)    
    current_sum = 0
    i += 1
    j += 1
    if j == len(arr):
        break

print(max_sum)
    
#