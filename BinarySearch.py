nums = [1,3,3,4,5,6]
target = 5
count = 0
for x in range(0, len(nums)):
    if x == target:
        print(count)
    count += 1