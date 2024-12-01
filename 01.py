def read_file():
    with open("01input.txt", "r") as file:
        data = file.readlines()

    return data

def parse_data(data):
    for line in data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    return list1, list2

def sum_distances(list1, list2):
    list1.sort()
    list2.sort()

    distances=[]
    for n in range(len(list1)):
        distance = abs(list1[n] - list2[n])
        distances.append(distance)

    return sum(distances)

def similarity_score(list1, list2):
    similarity_scores=[]
    for n in range(len(list1)):
        multiplier = list2.count(list1[n])
        similarity_scores.append(list1[n] * multiplier)
    return sum(similarity_scores)
        

def main():
    list1=[]
    list2=[]

    data = read_file()
    list1, list2 = parse_data(data)
    part1 = sum_distances(list1, list2)
    part2 = similarity_score(list1, list2)
    print(part1)
    print(part2)








if __name__ == "__main__":
    main()
