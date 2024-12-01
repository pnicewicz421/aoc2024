list1=[]
list2=[]
distances=[]

with open("01input.txt", "r") as file:
    data = file.readlines()

    for line in data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    list1.sort()
    list2.sort()

    for n in range(len(list1)):
        distance = abs(list1[n] - list2[n])
        distances.append(distance)

    print(sum(distances))

    

