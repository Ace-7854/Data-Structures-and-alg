def reverse_array(arr):
    return arr[::-1]

def smallest_and_largest(arr):
    if not arr:
        return None, None
    smallest = min(arr)
    largest = max(arr)
    return smallest, largest    

def sum_of_n(arr):
    return sum(arr)