def get_middle(search_list):
    if not search_list:
        return None    
    length = len(search_list)
    middle_index = (length - 1) // 2
    return search_list[middle_index]
    
def find(search_list: list, value: int)-> list:
    sorted_list = sorted(search_list)
    current_list = sorted_list[:]
    
    while current_list:
        middle_value = get_middle(current_list)
        mid_index = sorted_list.index(middle_value)
        if middle_value == value:
            return mid_index
        elif middle_value < value:
            right_half_index = current_list.index(middle_value) + 1
            current_list = current_list[right_half_index:]
        else:
            left_half_index = current_list.index(middle_value)
            current_list = current_list[:left_half_index]
    raise ValueError("value not in array")