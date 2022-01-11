import math
nums = [0,0,0,0,0,0,1,1,1,1]

max = len(nums)
notdone = True
min = 0
while True:
    
    if nums[math.floor(min+ ((max-min)/2))] == 1:
        max = math.floor(min + ((max-min)/2))
    else:
        min = math.floor(min + ((max-min)/2))

    if min + 1 == max:
        print(max)