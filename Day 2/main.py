with open('strategy.txt') as file:
    data = [i for i in file.read().strip().split('\n')]

# print(data)

win = 0
lose = 0
draw = 0
o_point = 0     # 1 point for x
t_point = 0     # 2 points for y
th_point = 0    # 3 points for z
total = 0

# part 2 says...
# a = rock;         x = lose
# b = paper;        y = Draw
# c = sissors;      z = Win

for game in data:
    if game[2] == 'Z':
        win += 6
    elif game[2] == 'Y':
        draw += 3

for game in data:
    if game[0] == 'A' and game[2] == 'X':           # lose
        th_point += 3
    elif game[0] == 'A' and game[2] == 'Y':         # draw
        o_point += 1
    elif game[0] == 'A' and game[2] == 'Z':         # Win
        t_point += 2
    elif game[0] == 'B' and game[2] == 'X':         # Lose
        o_point += 1
    elif game[0] == 'B' and game[2] == 'Y':         # Draw
        t_point += 2
    elif game[0] == 'B' and game[2] == 'Z':         # Win
        th_point += 3
    elif game[0] == 'C' and game[2] == 'X':         # Lose
        t_point += 2
    elif game[0] == 'C' and game[2] == 'Y':         # Draw
        th_point += 3
    elif game[0] == 'C' and game[2] == 'Z':         # Win
        o_point += 1
    
total = win + draw + lose + o_point + t_point + th_point

print(total)
