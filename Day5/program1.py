def read_seeds(text):
    # print(text)
    _, seeds_num = text.split(":")

    seeds_num = seeds_num.lstrip().rstrip()
    seeds_num = [int(num) for num in seeds_num.split(" ")]
    return seeds_num

def read_data(text):
    _, locations = text.split(":\n")
    locations = locations.split("\n")

    ret = []

    for loc in locations:
        loc = loc.split(" ")
        ret.append([int(x) for x in loc])

    return ret

def get_seeds_location(seed, data):

    elem = seed
    for map_ in data:
        for  destination_start, source_start, range_ in map_:
            if elem >= source_start and elem <= source_start + range_:
                
                offset = elem - source_start
                elem = destination_start + offset
                break

    return elem

with open("data.txt") as f:
    lines  = f.readlines()

    lines = "".join(lines)
    lines = lines.split("\n\n")
    # print(lines.split("\n\n"))
    seeds = read_seeds(lines[0])
    
    data = [read_data(lines[i]) for i in range(1,8)]
    # print(seeds)
    location = [get_seeds_location(seed, data) for seed in seeds]

print(min(location))
    