def create_lists():
    with open('input-day01.txt') as file:
        first_list = []
        second_list = []
        for line in file:
            elements = line.split()
            first_list.append(int(elements[0]))
            second_list.append(int(elements[1]))
        sorted_list1=sorted(first_list)
        sorted_list2=sorted(second_list)
    return sorted_list1, sorted_list2

def count_distance():
    sorted_list1, sorted_list2 = create_lists()
    distance = 0
    for e1, e2 in zip(sorted_list1, sorted_list2):
        if e1 > e2:
            distance += int(e1 - e2)
        elif e2 > e1:
            distance += int(e2 - e1)
        else:
            distance += 0
    return distance

def count_similarities():
    sorted_list1, sorted_list2 = create_lists()
    similarities = 0
    for element1 in sorted_list1:
        occurrence = sorted_list2.count(element1)
        similarities += (element1 * occurrence)
    return similarities


if __name__ == "__main__":
    print("---Part One---")
    print("Distance: ", count_distance())
    print("---Part Two---")
    print("Similarities: ", count_similarities())

