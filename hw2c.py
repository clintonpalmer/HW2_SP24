import copy
import math


def make_diagonal_dominant(Aaug):
    """
    In order to use the Gauss-Seidel method the matrix should
    be arranged in a diagonal dominant form. The function copies
    the matrix and stores it to B, this is done to prevent modifying
    the original matrix. The function iterates over each row (i)
    and determines the configuration of a diagonally dominant matrix.
    chatgpt assisted in developing this function
    """
    N = len(Aaug)
    B = copy.deepcopy(Aaug)  # makes a copy of the matrix
    for i in range(N):  # begins iterating through each row and column
        max_val = -math.inf
        max_index = -1
        for j in range(i, N):
            if abs(B[j][i]) > max_val:
                max_val = abs(B[j][i])
                max_index = j
        if i != max_index:
            B[i], B[max_index] = B[max_index], B[i]
    return B


def GaussSeidel(Aaug, x, Niter=15):
    """
    This function takes 3 arguments Aaug, x, and Niter
    :param N: gathers number of rows in matrix
    :param Aaug: augmented matrix
    :param x: initial guess
    :param Niter: number of iterations
    :Aaug[i]: storage for coefficients in the equations
    :return x: returns the solution to the x in main()
    chatgpt assisted in developing this function
    """
    N = len(Aaug)
    for _ in range(Niter):
        x_old = copy.deepcopy(x)  # makes copy of current solution vector x
        for i in range(N):
            temp = Aaug[i][-1]
            for j in range(N):
                if i != j:
                    temp -= Aaug[i][j] * x_old[j]
            x[i] = temp / Aaug[i][i]  # creates new value for x variable
        x = [round(num, 3) for num in x]  # rounds each number to 3 decimal places
    return x


def main():
    """
    The main function is going to estimate the x values in a set
    of linear equations using the Gauss-Seidel method.
    :Aaug: augmented matrix [A|b]
    chatgpt assisted in developing this function
    """
    # 3 x 4 Augmented Matrix
    Aaug = [[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]]
    Aaug = make_diagonal_dominant(Aaug)  # pushes the Aaug matrix to the make_diagonal_dominant function
    x = [0, 0, 0]  # initial guess
    x = GaussSeidel(Aaug, x)  # pushes the initial guess to the GaussSeidel function
    print(f"The solutions are {x}")

    # 4 x 5 Augmented Matrix
    Aaug = [[1, -10, 2, 4, 2], [3, 1, 4, 12, 12], [9, 2, 3, 4, 21], [-1, 2, 7, 3, 37]]
    Aaug = make_diagonal_dominant(Aaug)  # pushes the Aaug matrix to the make_diagonal_dominant function
    x = [0, 0, 0, 0]  # initial guess
    x = GaussSeidel(Aaug, x)  # pushes the initial guess to the GaussSeidel function
    print(f"The solutions are {x}")


main()
