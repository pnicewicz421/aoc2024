import re

def read_file():
    with open("03input.txt", "r") as file:
        data = file.read()
    return data

def sum_valid_multiplications(data):
    pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
   
    matches = re.findall(pattern, data)
    
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

def sum_enabled_multiplications(data):
    mul_pattern = r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    mul_enabled = True
    total_sum = 0
    
    tokens = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', data)
    
    for token in tokens:
        if type(token)==str:        
            if re.match(do_pattern, token):
                mul_enabled = True
            elif re.match(dont_pattern, token):
                mul_enabled = False
            else:
                match = re.match(mul_pattern, token)
                if match and mul_enabled:
                    x, y = match.groups()
                    total_sum += int(x) * int(y)
        
    return total_sum

def main():
    data = read_file()
    part1 = sum_valid_multiplications(data)
    part2 = sum_enabled_multiplications(data)
    print(part1)
    print(part2)
    

if __name__ == "__main__":
    main()
