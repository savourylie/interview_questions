def quick_sort(lst):
    if len(lst) < 2:
        return lst

    pivot = lst[0]

    smaller = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    larger = [x for x in lst if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)

# def quick_sort(lst):
#     N = len(lst)
#
#     if N < 2:
#         return lst
#
#     if N == 2:
#         if lst[0] > lst[1]:
#             return lst[::-1]
#         else:
#             return lst
#
#     mid = N // 2
#     pivot = lst[mid]
#     is_sorted = True
#
#     i, j = 0, N - 1
#
#
#     while i <= j:
#         while lst[i] < pivot:
#             i += 1
#         while lst[j] >= pivot:
#             j -= 1
#
#         if i <= j:
#             lst[i], lst[j] = lst[j], lst[i]
#             i += 1
#             j -= 1
#             is_sorted = False
#
#     if is_sorted:
#         return lst
#
#     return quick_sort(lst[:i]) + quick_sort(lst[i:])

if __name__ == '__main__':
    lst1 = [1, 5, 4, 1, 6, 3, 52, 5, 23, 5, 6]
    lst2 = [4, 542, 55, 24, 245, 645, 14, 7, 4]
    lst3 = [4, 542, 55, 24, 245, 645, 14, 7, 4] + [4, 542, 55, 24, 245, 645, 14, 7, 4] + lst1

    assert quick_sort(lst1) == sorted(lst1)
    assert quick_sort(lst2) == sorted(lst2)
    assert quick_sort(lst3) == sorted(lst3)
