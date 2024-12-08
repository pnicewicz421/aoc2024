from itertools import product

part1_operators = ['+', '*']
part2_operators = ['+', '*', '||']

def concat_nums(a, b):
    return int(str(a) + str(b))

def part1_calc(k, nums):
    for ops in product(part1_operators, repeat=len(nums)-1):
        current = nums[0]
        for num, op in zip(nums[1:], ops):
            if op == '+':
                current += num
            else:
                current *= num
        if current == k:
            return k
    return 0

def part2_calc(k, nums):
    for ops in product(part2_operators, repeat=len(nums)-1):
        current = nums[0]
        for num, op in zip(nums[1:], ops):
            if op == '+':
                current += num
            elif op == '*':
                current *= num
            else:  # op == '||'
                current = concat_nums(current, num)
                
        if current == k:
            return k
    return 0

def read_file(data):
    calcs = {}
    with open('07input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            chars = line.split(':')
            k = int(chars[0].strip())
            v = [int(i) for i in chars[1].strip().split(' ')]
            calcs[k] = v        
    return calcs

def main():
    data = read_file('07input.txt')
    part1 = 0
    for k, v in data.items():
        result = part1_calc(k, v)
        if result > 0:
            part1 += result
    print(part1)

    part2 = 0
    for k, v in data.items():
        result = part2_calc(k, v)
        if result > 0:
            part2 += result
    print(part2)

if __name__ == "__main__":
    main()
