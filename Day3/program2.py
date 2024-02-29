import numpy as np

with open("data.txt") as f:
    lines = f.readlines()

    index = 0
    is_prev_digit = False
    numbers = []
    gear_map = []

    for j, line in enumerate(lines):
        map_line = []
        num = ""
        line = line.replace("\n","")
        for i, c in enumerate(line):
            if c.isdigit():
                is_prev_digit = True
                map_line.append(index)
                num += c
            else:
                map_line.append(c)
                if is_prev_digit:
                    numbers.append(int(num))
                    num = ""
                    is_prev_digit = False
                    index+=1

        if is_prev_digit:
                numbers.append(int(num))
                num = ""
                is_prev_digit = False
                index+=1
        gear_map.append(map_line)



to_sum = []
for i, line in enumerate(gear_map):
    for j, c in enumerate(line):
        if type(c) == str and c != ".":
            nums = set()
            # print(i,j,c)
            if j > 0 and type(line[j-1]) == int:
                nums.add(numbers[line[j-1]])
            
            if j < len(line) and type(line[j+1]) == int:
                nums.add(numbers[line[j+1]])
            
            if i > 0 and type(gear_map[i-1][j]) == int:
                nums.add(numbers[gear_map[i-1][j]])
            
            if i < len(gear_map) and type(gear_map[i+1][j]) == int:
                nums.add(numbers[gear_map[i+1][j]])

            if i > 0 and j > 0 and type(gear_map[i-1][j-1]) == int:
                nums.add(numbers[gear_map[i-1][j-1]])
            
            if i < len(gear_map) and j > 0 and type(gear_map[i+1][j-1]) == int:
                nums.add(numbers[gear_map[i+1][j-1]])

            if i > 0 and j < len(line) and type(gear_map[i-1][j+1]) == int:
                nums.add(numbers[gear_map[i-1][j+1]])
            
            if i < len(gear_map) and j < len(line) and type(gear_map[i+1][j+1]) == int:
                nums.add(numbers[gear_map[i+1][j+1]])

            nums = list(nums)
            if len(nums) == 2:
                to_sum.append(nums[0] * nums[1])

print(np.sum(to_sum))

