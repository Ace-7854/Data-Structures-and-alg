import random

def main(): 
    
    # user = input("Enter the numbers with spaces between them: ")
    # numbers = user.split()

    numbers = [random.randint(1,100) for _ in range(10)]

    numbers.sort()
    print(f"smallest: {numbers[0]}, largest: {numbers[-1]}")

    sum_of_n = sum(map(int, numbers))
    print(f"sum: {sum_of_n}")
    
    print(reverse_array(numbers))

def reverse_array(arr):
    return arr[::-1]
    


if __name__ == "__main__":    
    main()