def merge_sort(li: list, reverse: bool=False) -> list:
    if len(li) < 2:
        return li
    
    half = len(li) // 2
    sorted_left_side = merge_sort(li[:half], reverse)
    sorted_right_side = merge_sort(li[half:], reverse)
    return merge(sorted_left_side, sorted_right_side, reverse)


def merge(first: int, second: int, reverse: bool=False) -> list:
        
    final = []
    i, j = 0, 0

    if not reverse:
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1

    else:
        while i < len(first) and j < len(second):
            if first[i] >= second[j]:
                final.append(first[i])
                i += 1
            else:
                final.append(second[j])
                j += 1

    while i < len(first):
        final.append(first[i])
        i += 1

    while j < len(second):
        final.append(second[j])
        j += 1
    
    return final
