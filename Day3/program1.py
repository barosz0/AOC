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


flags = [False for _ in range(len(numbers))]

for i, line in enumerate(gear_map):
    for j, c in enumerate(line):
        if type(c) == str and c != ".":
            if j > 0 and type(line[j-1]) == int:
                flags[line[j-1]] = True
            
            if j < len(line) and type(line[j+1]) == int:
                flags[line[j+1]] = True
            
            if i > 0 and type(gear_map[i-1][j]) == int:
                flags[gear_map[i-1][j]] = True
            
            if i < len(gear_map) and type(gear_map[i+1][j]) == int:
                flags[gear_map[i+1][j]] = True

            if i > 0 and j > 0 and type(gear_map[i-1][j-1]) == int:
                flags[gear_map[i-1][j-1]] = True
            
            if i < len(gear_map) and j > 0 and type(gear_map[i+1][j-1]) == int:
                flags[gear_map[i+1][j-1]] = True

            if i > 0 and j < len(line) and type(gear_map[i-1][j+1]) == int:
                flags[gear_map[i-1][j+1]] = True
            
            if i < len(gear_map) and j < len(line) and type(gear_map[i+1][j+1]) == int:
                flags[gear_map[i+1][j+1]] = True

numbers = np.array(numbers)
print(np.sum(numbers[flags]))

