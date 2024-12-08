def read_file():
    grid = {}
    with open('08input.txt', 'r') as file:
        y = 0
        x = 0
        for y, line in enumerate(file):
            for x, char in enumerate(line):
                if char != '.' and char != '\n':
                    if char not in grid:
                        grid[char] = [(y, x)]
                    else:
                        grid[char].append((y,x))
    return grid, y+1, x+1



def place_antidote(p1, p2, y_max, x_max, antidotes, part2=False):
    # Get the vector between the two points
    dx = p2[1] - p1[1]  # horizontal
    dy = p2[0] - p1[0]  # vertical
    
    if dx == 0 and dy == 0:
        return
    
    # Antinodes from p1
    s = 1
    while True:
        y1 = p1[0] + dy*s
        x1 = p1[1] + dx*s
        if 0 <= y1 < y_max and 0 <= x1 < x_max:
            antidotes.add((y1, x1))
            if part2:
                s += 1
            else:
                break
        else:
            break
    
    # Antinodes from p2
    p = 1
    while True:
        y2 = p2[0] - dy*p
        x2 = p2[1] - dx*p
        if 0 <= y2 < y_max and 0 <= x2 < x_max:
            antidotes.add((y2, x2))
            if part2:
                p += 1
            else:
                break
        else:
            break


def main():
    part1set = set()
    part2set = set()
    grid, y_max, x_max = read_file()
    for k in grid:
        for idx, (y1, x1) in enumerate(grid[k]):
            if idx == len(grid[k]) - 1:
                break
            for (y2, x2) in grid[k][idx+1:]:
                place_antidote((y1, x1), (y2, x2), y_max, x_max, part1set)
                place_antidote((y1, x1), (y2, x2), y_max, x_max, part2set, part2=True)
    print(len(part1set))
    print(len(part2set))    

if __name__ == '__main__':
    main()
    

