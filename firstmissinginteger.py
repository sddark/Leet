arr = [ 3, 4, -1, 1 ]

arr.sort()

for i in range(0, len(arr) - 1):
    if arr[i] > 0:
        if arr[i] != arr[i+1] and arr[i]!= arr[i+1] + 1: 
            print(arr[i] + 1)
            break
