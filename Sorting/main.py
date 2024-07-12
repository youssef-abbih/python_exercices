from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def get_sorting_algorithm(choice, numbers, reverse):
    if choice in ["s", "selection"]:
        return "Selection Sort", selection_sort(numbers, reverse=reverse)
    elif choice in ["b", "bubble"]:
        return "Bubble Sort", bubble_sort(numbers, reverse=reverse)
    elif choice in ["i", "insertion"]:
        return "Insertion Sort", insertion_sort(numbers, reverse=reverse)
    elif choice in ["m", "merge"]:
        return "Merge Sort", merge_sort(numbers, reverse=reverse)
    elif choice in ["q", "quick"]:
        quick_sort(numbers, 0, len(numbers) - 1)
        return "Quick Sort", numbers
    elif choice in ["e", "exit"]:
        return "Exit", None
    else:
        return "Invalid choice", None


def main() -> None:
    numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,
               918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767,
               553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

    while True:
        choice = input("Select a sorting algorithm (s: Selection, b: Bubble, i: Insertion, m: Merge, q: Quick, e: Exit): ")

        if choice.lower() == "e" or choice.lower() == "exit":
            break

        if choice.lower() not in ["s", "selection", "b", "bubble", "i", "insertion", "m", "merge", "q", "quick"]:
            print("Invalid choice. Please try again.")
            continue

        order = input("Order (ASC or DESC): ") if choice.lower() != "e" else None
        reverse = True if order and order.upper() == "DESC" else False

        algorithm_name, sorted_numbers = get_sorting_algorithm(choice.lower(), numbers.copy(), reverse)

        if algorithm_name == "Exit":
            break
        elif algorithm_name == "Invalid choice":
            print("Invalid choice. Please try again.")
            continue

        print(f"{algorithm_name} ({'Descending' if reverse else 'Ascending'} Order):")
        print(sorted_numbers)
        print()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()