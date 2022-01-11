arr = [1,2,3,4,5]
target = 6
prev=1
def multiplyarray(arr, target):
    prev = 1
    for i in range(0, len(arr)):
        if i != target:
            prev = prev * arr[i]
    return prev

print(multiplyarray([1,2,3,4,5],3))