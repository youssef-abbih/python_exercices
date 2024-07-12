def insertion_sort(li: list, reverse: bool=False)->list:

    def compare(a: int|float, b: int|float)->bool:
        return a < b if reverse else a > b

    if len(li) <= 2:
        return li
        
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while(j >= 0 and compare(li[j], key)):
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
    return li