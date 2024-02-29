import numpy as np
import copy
num = ["1","2","3","4","5","6","7","8","9"]
num_char = ["1","2","3","4","5","6","7","8","9"] #["one","two","three","four","five","six","seven","eight","nine"] # second task

num = num+num_char

aim = []

with open("data.txt") as f:
    for line in f.readlines():
        line_org = line.replace("\n","")
        nums_index = []
        

        for c in num:
            line = copy.copy(line_org)
            index = []
            if line.find(c)>=0:

                index = [line.find(c),line.find(c)]

                while line.find(c)>=0:
                    index[1] = line.find(c)
                    line = line.replace(c,"x"*len(c),1)
                    
                
            else:
                index = [-1,-1]
            nums_index.append(index)

        nums_min = np.array(nums_index)[:,0]
        nums_min[nums_min<0] = 999999
        nums_min = np.min([nums_min[:9],nums_min[9:]],0)

        nums_max = np.array(nums_index)[:,1]
        nums_max = np.max([nums_max[:9],nums_max[9:]],0)
        
        # print(nums_index)
        # print(line)


        print(np.argmin(nums_min)+1, np.argmax(nums_max)+1)
        liczba = 10 * (np.argmin(nums_min)+1) + np.argmax(nums_max)+1
        aim.append(liczba)


# nums_min =np.array( [nums_index[:9,0], nums_index[9:,0]])

print(sum(aim))

