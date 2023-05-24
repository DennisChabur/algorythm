import random as rd


def random_number_list(length):
    rand_arr = []
    for i in range(length):
        n = round(rd.randint(-100, 100))
        rand_arr.append(n)
    # return rand_arr
    return rand_arr


def bubble_sort(random_list):
    length = len(random_list)
    while length > 1:
        for i in range(length - 1):
            if random_list[i] > random_list[i+1]:
                temp = random_list[i+1]
                random_list[i+1] = random_list[i]
                random_list[i] = temp
        length -= 1
    return random_list


def quick_sort(random_list):
    length = len(random_list)
    if length <2: return random_list
    pivot = random_list[-1]
    smaller_arr, larger_arr = [], []
    for i in random_list[:-1]:
        if i <= pivot: smaller_arr.append(i)
        else: larger_arr.append(i)
    return quick_sort(smaller_arr) + [pivot] + quick_sort(larger_arr)


def heapify(random_list, heap_size, root_index):
    largest_index = root_index
    left_child_index = 2 * root_index + 1
    right_child_index = 2 * root_index + 2

    if left_child_index < heap_size and random_list[root_index] < random_list[left_child_index]:
        largest_index = left_child_index
    if right_child_index < heap_size and random_list[largest_index] < random_list[right_child_index]:
        largest_index = right_child_index
    if largest_index != root_index:
        (random_list[root_index], random_list[largest_index]) = (random_list[largest_index], random_list[root_index])


def heap_sort(random_list):
    length = len(random_list)

    for i in range(length // 2 - 1, -1, -1):
        heapify(random_list, length, i)

    for i in range(length - 1, 0, -1):
        random_list[0], random_list[i] = random_list[i], random_list[0]
        heapify(random_list, i, 0)


print(bubble_sort(random_number_list(10)))

print(quick_sort(random_number_list(10)))

print(heap_sort(random_number_list(10)))

