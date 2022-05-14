list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]


def multiplylist_indices (list_1, list_2):
    empty_list = []
    if len(list_1) != len(list_2):
        print("Please use lists that are of equal lengths. \n*END of execution*")
    else:
        for elements in range(0, len(list_1)):
            empty_list.append(list_1[elements] * list_2[elements])
    return empty_list


print(multiplylist_indices(list_1, list_2))