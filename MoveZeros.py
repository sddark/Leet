nums = [0,0]
y=0
if len(nums) > 1:
    for x in range (0, len(nums)):
        if y >= len(nums):
            nums[x] = 0 
        elif y == len(nums)-1:
            if x != y:
                nums[x] = nums[y]
        elif nums[y] == 0:
            while nums[y] ==0:
                if y <= len(nums) - 2:
                    y +=1
                else:
                    break
            nums[x] = nums [y]
        else:
            nums[x] = nums [y]

        y += 1