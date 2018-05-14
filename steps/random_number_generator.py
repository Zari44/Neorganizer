import random

if __name__ == "__main__":
    number_of_circles = 3
    community_members = ['a','b','c','d','e','f','g']
    circles = [[] for x in range(number_of_circles)]
    number_of_members = len(community_members)
    picked_indices = []
    while len(picked_indices) < number_of_members:
        for i in range(number_of_circles):
            if len(picked_indices) < number_of_members:
                index = random.randrange(number_of_members)
                while (index in picked_indices):
                    index = random.randrange(number_of_members)
                picked_indices.append(index)
                print(picked_indices)
                circles[i].append(community_members[index])

    print("final print:")
    for circle in circles:
        print("--- circle ---")
        for member in circle:
            print(member)
