nums = [1,2,3,4,5,6,7]
k = 15
j = k%len(nums)
count = 0
z= len(nums)
while count < k:
    for x in range(0, len(nums)):
        if x ==0:
            y = nums[x+1]
            nums[x+1] = nums[x]
        elif x == len(nums)-1:
            nums[0] = y
        else:
            temp = nums[x+1]
            nums[x+1] = y
            y = temp

    count += 1
print(nums)