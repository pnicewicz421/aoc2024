def read_map(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.rstrip('\n')))
    return grid

def start_position(grid):
    directions = {'^': 0, '>': 1, 'v': 2, '<': 3}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return (x, y), directions[cell]
    return None, None  

def move_player(grid, obstruction_pos=None):
    width = len(grid[0])
    height = len(grid)
    
    dir_moves = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]  # (dx, dy)
        
    (x, y), dir = start_position(grid)
            
    if obstruction_pos:
        ox, oy = obstruction_pos
        grid[oy][ox] = '#'
    
    visited_states = set()
    visited_positions = set()
    
    while True:
        state = (x, y, dir)
        if state in visited_states:
            # loop detected
            loop_detected = True
            break
        visited_states.add(state)
        visited_positions.add((x, y))
        
        # calculate next position
        dx, dy = dir_moves[dir]
        nx, ny = x + dx, y + dy
        
        # check if next position is out of bounds
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            loop_detected = False
            break
        
        next_cell = grid[ny][nx]
        if next_cell == '#':
            # obstacle ahead, rotate
            dir = (dir + 1) % 4
        else:
            # move forward
            x, y = nx, ny
    
    # remove obstruction 
    if obstruction_pos:
        ox, oy = obstruction_pos
        grid[oy][ox] = '.'
    
    return loop_detected

def count_part2(grid):
    width = len(grid[0])
    height = len(grid)
    valid_positions = 0
    
    # starting position 
    (start_x, start_y), _ = start_position(grid)
    
    # test all valid positions 
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '.' and (x, y) != (start_x, start_y):
                loop_detected = move_player(grid, obstruction_pos=(x, y))
                if loop_detected:
                    valid_positions += 1
    return valid_positions

def main():
    grid = read_map('06input.txt')
    
    positions_visited = move_player(grid)
    print(len(positions_visited))
    
    total_valid_positions = count_part2(grid)
    print(total_valid_positions)

if __name__ == "__main__":
    main()
