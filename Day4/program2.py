cards = []

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
        
        cards.append([winning_numbers,your_numbers,nums])
        

amount = [1 for _ in range(len(cards))]

for j, (_,_,nums) in enumerate(cards):
    for i in range(len(nums)):
        amount[j+i+1] += amount[j]

print(sum(amount))