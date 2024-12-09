def read_file():
    with open('09input.txt', 'r') as file:
        return file.read()

def map_file(data):
    reformat = []
    id = 0 
    for i, c in enumerate(data):
        if i % 2 == 0:
            reformat += [id] * int(c)
            id += 1
        else:
            reformat += ['.'] * int(c) 
    return reformat

def is_sorted(data):
    for i in range(data.index('.'), len(data)):
        if data[i] != '.':
            return False
    return True

def move_data1(data):
    moved_data = data.copy()
    dot_pos = moved_data.index('.')  

    for i in range(len(data)-1, -1, -1):
        if moved_data[i] != '.':
            if i > dot_pos:  
                moved_data[dot_pos], moved_data[i] = moved_data[i], '.'
                dot_pos = moved_data.index('.', dot_pos + 1)
    
    return moved_data

def get_dot_locs(data):
    indot = False 
    dotsize = 0 
    dot_locs = []
    for dot_pos in range(len(data)):
        if data[dot_pos] == '.':
            if indot:
                dotsize += 1 
            else:
                indot = True    
                dotsize = 1
        elif data[dot_pos] != '.' and indot:
            indot = False
            dot_locs.append((dot_pos - dotsize, dotsize))
            dotsize = 0
    if indot:
        dot_locs.append((dot_pos - dotsize, dotsize))
    
    return dot_locs

def get_file_locs(data):
    num_locs = []
    innum = False
    numsize = 0
    numval = -1
    start_pos = 0
    for pos in range(len(data)):
        if data[pos] != '.':
            if data[pos] == numval:
                numsize += 1
            else:
                if innum:
                    num_locs.append((numsize, numval, start_pos))
                numval = data[pos]
                numsize = 1
                start_pos = pos
                innum = True
        else:
            if innum:
                num_locs.append((numsize, numval, start_pos))
                innum = False
                numsize = 0
                numval = -1
    if innum:
        num_locs.append((numsize, numval, start_pos))
    num_locs.sort(key=lambda x: x[1], reverse=True)
    return num_locs

def move_data2(data, num_locs, dot_locs):
    moved_data = data.copy()
    new_dot_locs = dot_locs.copy()
    for file_info in num_locs:
        numsize, numval, numpos = file_info
        print(f"Trying to move file {numval} starting at {numpos} with size {numsize}")
        
        suitable_dot_idx = -1
        for idx, dot_info in enumerate(new_dot_locs):
            dotpos, dotsize = dot_info
            if dotsize >= numsize and dotpos < numpos:
                suitable_dot_idx = idx
                break  

        if suitable_dot_idx != -1:
            dotpos, dotsize = new_dot_locs[suitable_dot_idx]
            
            for k in range(numsize):
                moved_data[dotpos + k] = numval
                moved_data[numpos + k] = '.'
            print(f"Moved file {numval} to position {dotpos}")

            if dotsize == numsize:
                new_dot_locs.pop(suitable_dot_idx)
            else:
                
                new_dot_locs[suitable_dot_idx] = (dotpos + numsize, dotsize - numsize)
        else:
            print(f"Cannot move file {numval}; no suitable free space to the left.")
    return moved_data
    

def checksum(data):
    checksum = 0
    for i, e in enumerate(data):
        if type(e) == int:
            checksum += i * e 
    return checksum
   

def main():
    data = read_file()
    data = map_file(data)
    
    data1 = move_data1(data)
    print(checksum(data1))

    dot_locs = get_dot_locs(data)
    num_locs = get_file_locs(data)  
    data2 = move_data2(data, num_locs, dot_locs)
    print(checksum(data2))


if __name__ == "__main__":
    main()  
