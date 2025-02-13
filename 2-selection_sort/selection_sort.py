def search_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    new_arr = []

    for _ in range(len(arr)):
        smallest = search_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


print(selection_sort([5, 32, 4, 7, 1, 10, 24]))

