def bubble_sort(li: list, reverse: bool=False)->list:
    swapped = True
    end = len(li)
    
    def compare(a: int|float, b: int|float)->bool:
        return a > b if not reverse else a < b

    if len(li) <= 2:
        return li

    while swapped:
        swapped = False
        for i in range(end-1):
            if compare(li[i], li[i+1]):
                li[i], li[i+1] = li[i+1], li[i]
                swapped = True
        end -= 1
    return li