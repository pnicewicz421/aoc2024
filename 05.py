import re
import numpy as np
from collections import defaultdict, deque

def read_file():
    rules = []
    updates = []
    with open("05input.txt", "r") as file:
        for line in file:
            if '|' in line:
                rules.append(line.strip().split('|'))
            if ',' in line:
                updates.append(line.strip().split(','))

        order_dict = {}
        for i in range(len(rules)):
            if int(rules[i][0]) not in order_dict:
                order_dict[int(rules[i][0])] = [int(rules[i][1])]
            else:
                order_dict[int(rules[i][0])].append(int(rules[i][1]))    

        updates = [[int(x) for x in update] for update in updates]

    return order_dict, updates

def verify_sequence(sequence, order_dict):
    for i, e in enumerate(sequence):
        if False in [elem in order_dict[e] for elem in sequence[i+1:]]:
            return False
    return True

def get_middle_number(sequence):
    return sequence[len(sequence)//2]

def fix_sequence(sequence, order_dict):
    if verify_sequence(sequence, order_dict):
        return sequence
    else:
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                if sequence[j] not in order_dict.get(sequence[i], []):
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                    if verify_sequence(sequence, order_dict):
                        return sequence
                    sequence[i], sequence[j] = sequence[j], sequence[i]
    
    return sequence

def main():
    order_dict, updates = read_file()
    part1_total = 0
    part2_total = 0

    for update in updates:
        if verify_sequence(update, order_dict):
            part1_total += get_middle_number(update)
        else:
            print(update)
            part2_total += get_middle_number(fix_sequence(update, order_dict))


    print(part1_total)
    print(part2_total)
    

if __name__ == "__main__":
    main()
