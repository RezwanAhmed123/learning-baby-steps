import random


def unique_maker(number_of_lists, list_size):
    master_list = []
    for a in range(number_of_lists):
        small_list = []
        for b in range(list_size):
            b = random.randint(1, 20)
            small_list.append(b)
            master_list.append(b)
        print(small_list)

    list_of_overlaps = []

    for number in master_list:
        number_count = master_list.count(number)
        if number_count > 1:
            if number not in list_of_overlaps:
                list_of_overlaps.append(number)
    print(list_of_overlaps)


client_number_of_lists = int(input("How many list numbers do you want to check?: "))
client_list_size = int(input("How many lists should be in each list?: "))
unique_maker(client_number_of_lists, client_list_size)
