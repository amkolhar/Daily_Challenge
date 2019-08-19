for height in range(len(grid)):
    for width in range(len(grid[height])):
        if grid[height][width] == color:
            new_beliefs[height][width] = p_hit * beliefs[height][width]
        else:
            new_beliefs[height][width] = p_miss * beliefs[height][width]

total = 0
for i in new_beliefs:
    total = total + sum(i)

for height in range(len(grid)):
    for width in range(len(height)):
        new_beliefs[height][width] = new_beliefs[height][width] / total