def quick_sort(li: list, start: int, end: int, reverse: bool=False) -> None:

    if start < end:
        pivot_index = partition(li, start, end, reverse)
        quick_sort(li, start, pivot_index - 1, reverse)
        quick_sort(li, pivot_index + 1, end, reverse)

def partition(li: list, start: int, end: int, reverse: bool=False) -> int:
    pivot = li[end]
    pivot_index = start

    for i in range(start, end):
        if (li[i] < pivot and not reverse) or (li[i] > pivot and reverse):
            li[i], li[pivot_index] = li[pivot_index], li[i]
            pivot_index += 1
            
    li[pivot_index], li[end] = li[end], li[pivot_index]
    return pivot_index
