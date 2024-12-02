def read_file():
    with open("02input.txt", "r") as file:
        data = []
        for line in file.readlines():
            row = [int(x) for x in line.strip().split()]
            data.append(row)

    return data

def is_safe(nums):
    if len(nums) <= 1:
        return True
    
    def check_sequence(index, is_increasing):
        if index >= len(nums) - 1:
            return True
            
        diff = nums[index + 1] - nums[index]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
           
        if (is_increasing and diff > 0) or (not is_increasing and diff < 0):
            return check_sequence(index + 1, is_increasing)
        return False
    
    # First case
    first_diff = nums[1] - nums[0]
    if abs(first_diff) < 1 or abs(first_diff) > 3:
        return False
        
    return check_sequence(0, first_diff > 0)

def is_safe_with_dampener(nums):
    if is_safe(nums):
        return True
            
    for i in range(len(nums)):
        dampened_nums = nums[:i] + nums[i+1:]
        if is_safe(dampened_nums):
            return True
            
    return False

def safe_count(data):
    count = 0
    for line in data:
        if is_safe(line):
            count += 1
    return count

def safe_count_with_dampener(data):
    count = 0
    for line in data:
        if is_safe_with_dampener(line):
            count += 1
    return count

def main():
    data = read_file()
    
    original_safe = safe_count(data)
    print(f"Safe count: {original_safe}")
        
    dampened_safe = safe_count_with_dampener(data)
    print(f"Safe count with dampener: {dampened_safe}")
    

if __name__ == "__main__":
    main()

