# For array of length 3
arr = [20, 90, 20]
# Sort without loops or recursion
if arr[0] > arr[1]:
  arr[0], arr[1] = arr[1], arr[0]
if arr[0] > arr[2]:
  arr[0], arr[2] = arr[2], arr[0]
if arr[1] > arr[2]:
  arr[1], arr[2] = arr[2], arr[1]

print(arr)