def merge_max_occ(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    mid_index = int(len(arr) / 2)
    current_element = arr[mid_index]

    prev_index = mid_index - 1
    prev_element = arr[prev_index]

    next_index = mid_index + 1
    if next_index < len(arr):
        next_element = arr[next_index]
    else:
        next_element = None
        next_index = len(arr)

    prev_occ = 0
    next_occ = 0

    while prev_element == current_element:
        prev_occ += 1
        prev_index -= 1

        if prev_index >= 0:
            prev_element = arr[prev_index]
        else:
            break

    while next_element == current_element:
        next_occ += 1
        next_index += 1

        if next_index < len(arr):
            next_element = arr[next_index]
        else:
            break

    return max(merge_max_occ(arr[:prev_index + 1]), prev_occ + 1 + next_occ, merge_max_occ(arr[next_index:]))


test_arr1 = [1]

print(merge_max_occ(test_arr1))