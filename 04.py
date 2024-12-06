import re
import numpy as np

def read_file():
    with open("04input.txt", "r") as file:
        data = file.read()
    return data

def get_data_array(data):   
    data_mapped = data.replace('X', '0').replace('M', '1').replace('A', '2').replace('S', '3')   
    rows = data_mapped.strip().split('\n')
    data_array = np.array([[int(char) if char in '0123' else -1 for char in row] for row in rows])
    return data_array

def count_xmas(data):
    data_array = get_data_array(data)
    horizontal_forward = sum(1 for i in range(len(data_array)) 
                    for j in range(len(data_array[i])-3) 
                    if all(data_array[i][j+k] == k for k in range(4)))
    vertical_forward = sum(1 for i in range(len(data_array)-3) 
                    for j in range(len(data_array[i])) 
                    if all(data_array[i+k][j] == k for k in range(4)))
    horizontal_backward = sum(1 for i in range(len(data_array)) 
                    for j in range(3, len(data_array[i])) 
                    if all(data_array[i][j-k] == k for k in range(4)))
    vertical_backward = sum(1 for i in range(3, len(data_array)) 
                    for j in range(len(data_array[i])) 
                    if all(data_array[i-k][j] == k for k in range(4)))
    diagonal_forward_down = sum(1 for i in range(len(data_array)-3) 
                    for j in range(len(data_array[i])-3) 
                    if all(data_array[i+k][j+k] == k for k in range(4)))
    diagonal_backward_down = sum(1 for i in range(3, len(data_array)) 
                    for j in range(len(data_array[i])-3) 
                    if all(data_array[i-k][j+k] == k for k in range(4)))
    diagonal_forward_up = sum(1 for i in range(len(data_array)-3) 
                    for j in range(3, len(data_array[i])) 
                    if all(data_array[i+k][j-k] == k for k in range(4)))
    diagonal_backward_up = sum(1 for i in range(3, len(data_array)) 
                    for j in range(3, len(data_array[i])) 
                    if all(data_array[i-k][j-k] == k for k in range(4)))

    return horizontal_forward + horizontal_backward + vertical_forward + vertical_backward + diagonal_forward_down + diagonal_backward_down + diagonal_forward_up + diagonal_backward_up

def count_xdashmas(data):
    data_array = get_data_array(data)
    count = 0

    for i in range(len(data_array)-2):

        for j in range(len(data_array[i])-2):
            if (data_array[i][j] == 1 and data_array[i][j+2] == 3):
                if data_array[i+1][j+1] == 2:
                    if (data_array[i+2][j] == 1 and data_array[i+2][j+2] == 3):
                        count += 1
            elif (data_array[i][j] == 1 and data_array[i][j+2] == 1):
                if data_array[i+1][j+1] == 2:
                    if (data_array[i+2][j] == 3 and data_array[i+2][j+2] == 3):
                        count += 1
            elif (data_array[i][j] == 3 and data_array[i][j+2] == 3):
                if data_array[i+1][j+1] == 2:
                    if (data_array[i+2][j] == 1 and data_array[i+2][j+2] == 1):
                        count += 1        
            elif (data_array[i][j] == 3 and data_array[i][j+2] == 1):
                if data_array[i+1][j+1] == 2:
                    if data_array[i+2][j] == 3 and data_array[i+2][j+2] == 1:
                        count += 1
    return count
                
               
    
def main():
    data = read_file()
    part1 = count_xmas(data)
    part2 = count_xdashmas(data)

    print(part1)
    print(part2)
    

if __name__ == "__main__":
    main()
