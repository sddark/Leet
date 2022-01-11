numbers = [2,7,11,15]
for x in range (0, len(numbers)):
    if x != 0:
        for y in range(x+1, len(numbers)):
            if numbers[x] + numbers[y] == target:
                print(x+1,y+1)