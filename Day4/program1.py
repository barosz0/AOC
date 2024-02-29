result = 0

with open("data.txt") as f:
    for line in f.readlines():
        _, card_part = line.split(":") 

        winning_numbers, your_numbers = card_part.split("|")

        winning_numbers = winning_numbers.split(" ")
        while "" in winning_numbers: winning_numbers.remove("")
        winning_numbers = [int(num) for num in winning_numbers]

        your_numbers = your_numbers.split(" ")
        while "" in your_numbers: your_numbers.remove("")
        your_numbers = [int(num) for num in your_numbers]


        nums = []
        for num in winning_numbers:
            if num in your_numbers:
                nums.append(nums)
        if len(nums) > 0:
            result += 2**(len(nums)-1)

print(result)
