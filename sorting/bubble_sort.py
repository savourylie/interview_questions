def bubble_sort(lst):
    is_sorted = False
    last_sorted_index = len(lst) - 1

    while not is_sorted:
        is_sorted = True

        for i in range(last_sorted_index):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False

        last_sorted_index -= 1

    return lst

if __name__ == '__main__':
    lst1 = [1, 5, 4, 1, 6, 3, 52, 5, 23, 5, 6]
    lst2 = [4, 542, 55, 24, 245, 645, 14, 7, 4]
    lst3 = [4, 542, 55, 24, 245, 645, 14, 7, 4] + [4, 542, 55, 24, 245, 645, 14, 7, 4] + lst1

    assert bubble_sort(lst1) == sorted(lst1)
    assert bubble_sort(lst2) == sorted(lst2)
    assert bubble_sort(lst3) == sorted(lst3)
