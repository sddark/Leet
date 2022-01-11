nums = [1,1,2]
nextP = 0
for i in range (0, len(nums)):
    if nums[i] != nums[nextP]:
        nextP += 1
        nums[nextP] = nums[i]     
print(nextP + 1)