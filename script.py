def binary_search(sorted_list, target):
    if not sorted_list:
        return "value not found"

    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]

    return mid_idx, mid_val
