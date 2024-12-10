def read_file():
    data = []
    with open('10input.txt', 'r') as file:
        for i, line in enumerate(file):
            data.append([])
            line = line.strip()
            for char in line:
                data[i].append(int(char))
    return data

def find_trails(starting_pos, data):
    full_trails = 0
    visited = set()
    queue = [(starting_pos, 0)]  
    
    while queue:
        current_pos, height = queue.pop(0)
        
        if height == 9:
            full_trails += 1
            continue
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
            new_x = current_pos[0] + dx
            new_y = current_pos[1] + dy
            new_pos = (new_x, new_y)
            
            if 0 <= new_x < len(data) and 0 <= new_y < len(data[0]):
                if data[new_x][new_y] == height + 1 and new_pos not in visited:
                    visited.add(new_pos)
                    queue.append((new_pos, height + 1))
    
    return full_trails


def find_trails2(starting_pos, data):
    paths = set()  
    queue = [(starting_pos, 0, ())]  
    
    while queue:
        current_pos, height, path = queue.pop(0)
        
        if height == 9:
            paths.add(path)  
            continue
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  
            new_x = current_pos[0] + dx
            new_y = current_pos[1] + dy
            new_pos = (new_x, new_y)
            
            if 0 <= new_x < len(data) and 0 <= new_y < len(data[0]):    
                if data[new_x][new_y] == height + 1 and new_pos not in path:
                    new_path = path + (new_pos,)
                    queue.append((new_pos, height + 1, new_path))
    
    return len(paths)  

def find_start_pos(data):
    start_pos = []
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == 0:
                start_pos.append((i, j))
    return start_pos

def main():
    data = read_file()
    start_positions = find_start_pos(data)
    total_score = 0
    
    for pos in start_positions:
        score = find_trails(pos, data)
        total_score += score
    
    print(f"Total score 1: {total_score}")

    start_positions = find_start_pos(data)
    total_score = 0

    for pos in start_positions:
        score = find_trails2(pos, data)
        total_score += score
    
    print(f"Total score 2: {total_score}")

if __name__ == '__main__':
    main()
