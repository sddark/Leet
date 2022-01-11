def findtwonumbers(arr, target):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] +arr[j] == target:
                return True
    return False

arr = [10,15,3,7]
k= 17
print(findtwonumbers(arr, k))
print(findtwonumbers([10,15,3,7], 30))
print(findtwonumbers([5, 5, 10,15,3,5], 10))