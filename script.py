def binary_search(sorted_list, target):
    if not sorted_list:
        return "value not found"

    mid_idx = len(sorted_list) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx

    if mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)
