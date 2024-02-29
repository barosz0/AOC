import numpy as np
games = []
balls_color_index = ["red", "green", "blue"]
games_index = []

with open("data2.txt") as f:
    for line in f.readlines():
        draws = line.replace("\n","").split(";")
        game_id, draws[0] = draws[0].split(":")
        game_id = game_id.split(" ")[-1]
        games_index.append(int(game_id))
        # r, g, b
        max_balls = [0,0,0]

        for draw in draws:
            draw = draw.split(",")
            for d in draw:
                num_balls, balls_color = d.lstrip().rstrip().split(" ")
                
                index = balls_color_index.index(balls_color.lower())

                max_balls[index] = max(max_balls[index], int(num_balls))

        games.append(max_balls)


games = np.array(games)

games_bool = (games<= np.array([12,13,14])).all(1)

print(np.sum(np.array(games_index) * games_bool))
