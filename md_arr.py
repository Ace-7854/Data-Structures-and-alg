import random

def main():
    matrix = make_matrix()
    matrix2 = make_matrix()
    display_matrix(matrix)
    print("\n")
    display_matrix(matrix2)
    print("\n")

    display_matrix(add_matrices(matrix, matrix2))
    

def display_matrix(matrix):
    for i in range(len(matrix)):
        print(f"{i}|{matrix[i]}")

def make_matrix():
    matrix = [[random.randint(1,100) for _ in range(3)] for _ in range(3)]
    return matrix

def add_matrices(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Matrices must be of the same size")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]    


if __name__ == "__main__":
    main()