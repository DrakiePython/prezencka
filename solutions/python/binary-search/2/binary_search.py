  

def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if value == search_list[middle]:
            return middle
        elif value < search_list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    raise ValueError("value not in array")
