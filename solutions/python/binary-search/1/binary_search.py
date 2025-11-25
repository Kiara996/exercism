def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    search_value = ""

    while left <= right:
        mid = (left + right) // 2
        mid_value = search_list[mid]

        if mid_value == value:
            search_value = mid
            return search_value
        elif mid_value < value:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("value not in array")