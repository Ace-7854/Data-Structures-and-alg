def linear_search(arr, target): 
    for i in range(len(arr)): 
        if arr[i] == target: 
            return i 
        
    return -1
    
def binary_search(arr, target):
    left, right = 0, len(arr) - 1 
    while left <= right: 
        mid = left + (right - left) //2
        if arr[mid] == target: 
            return mid 
        elif arr[mid] < target:
            left =mid + 1 
        else:
            right = mid - 1 
    return -1

def main(): 
    import random 
    arr = [random.randint(1,100) for _ in range(10)] 
    target = random.choice(arr) 
    print(f"Array: {arr}") 
    print(f"Target: {target}") 
    print(f"Linear Search Result: {linear_search(arr, target)}") 
    arr.sort() 
    print(f"Sorted Array: {arr}") 
    print(f"Binary Search Result: {binary_search(arr, target)}")


if __name__ == "__main__":
    main()