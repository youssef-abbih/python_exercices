def selection_sort(li: list, reverse: bool=False)->list:

    def compare(a: int|float, b: int|float)->bool:
        return a > b if reverse else a < b

    if len(li) <= 2:
        return li

    for i in range(len(li)):
        
        min_index = i
        
        for j in range(i + 1, len(li)):
            if compare(li[j], li[min_index]):
                min_index = j
        
        li[i], li[min_index] = li[min_index], li[i]
    return li

