def merge_sort(lst):
    N = len(lst)

    if N < 2:
        return lst
    if N == 2:
        if lst[0] > lst[1]:
            return lst[::-1]
        else:
            return lst

    return merge_sorted(merge_sort(lst[:N//2]), merge_sort(lst[N//2:]))

def merge_sorted(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    # len1, len2 = len(lst1), len(lst2)
    #
    # if len1 < len2:
    #     lst1, lst2 = lst2, lst1

    result_list = []

    while lst1 and lst2:
        current1, current2 = lst1[0], lst2[0]

        if current1 < current2:
            smaller = lst1.pop(0)
        else:
            smaller = lst2.pop(0)

        result_list.append(smaller)

    if len(lst1) > len(lst2):
        return result_list + lst1
    else:
        return result_list + lst2




if __name__ == '__main__':
    lst1 = [1, 5, 4, 1, 6, 3, 52, 5, 23, 5, 6]
    lst2 = [4, 542, 55, 24, 245, 645, 14, 7, 4]
    lst3 = [4, 542, 55, 24, 245, 645, 14, 7, 4] + [4, 542, 55, 24, 245, 645, 14, 7, 4] + lst1

    assert merge_sort(lst1) == sorted(lst1)
    assert merge_sort(lst2) == sorted(lst2)
    assert merge_sort(lst3) == sorted(lst3)

