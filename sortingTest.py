def insertion_sort(arr):
    """
    Sorts a list of integers using Insertion Sort.
    """
    if validation(arr):
        return arr
    
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        try:    
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        except TypeError:
            print(f"Error: Cannot compare {arr[j]} and {key}. Skipping comparison.")
            continue
    return arr


def bubble_sort(arr):
    """
    Sorts a list of integers using Bubble Sort.
    Returns True if already sorted, otherwise False.
    """
    if validation(arr):
        return arr

    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            try:    
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                    swapped = True
            except TypeError:
                print(f"Error: Cannot compare {arr[j]} and {arr[j + 1]}. Skipping comparison.")
                continue
        if not swapped:
            return True

    return False

def validation(arr):
    if arr is None or len(arr) == 0:
        return False
    elif not all(isinstance(x, int) for x in arr):
        return False
    


if __name__ == "__main__":
    import random
    arr = ["apple", "banana",6 ,"cherry", "date", "fig", "grape"]
    print(f'{insertion_sort(arr)}')
    print(f'{bubble_sort(arr)}')
    arr = [random.randint(1, 100) for _ in range(10)]
    print(f'{insertion_sort(arr)}')
    print(f'{bubble_sort(arr)}')
