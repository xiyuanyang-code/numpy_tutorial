import numpy as np

row = int(input("Please input the rows of matrix, which is the number of equations:"))
col = int(input("Please input the cols of matrix, which is the number of equations:"))

A = np.zeros((row, col))
b = np.zeros((row, 1))

def fillMatrix(A, b):
    """
    Fill the matrix A and vector b with user input.

    Parameters:
    A (numpy.ndarray): The matrix to be filled.
    b (numpy.ndarray): The vector to be filled.
    """
    for i in range(A.shape[0]):
        print(f"Fill in the {i + 1}th row of matrix A:")
        for j in range(A.shape[1]):
            while True:  # Loop until valid input is received
                try:
                    value = float(input(f"Enter value for A[{i},{j}]: "))  # Prompt for input
                    A[i, j] = value  # Assign value to matrix
                    break  # Exit the loop if input is valid
                except ValueError:  # Handle non-numeric input
                    print("Invalid input. Please enter a numeric value.")

    print("Fill in the vector b:")
    for i in range(b.shape[0]):
        while True:  # Loop until valid input is received
            try:
                value = float(input(f"Enter value for b[{i}]: "))  # Prompt for input
                b[i] = value  # Assign value to vector
                break  # Exit the loop if input is valid
            except ValueError:  # Handle non-numeric input
                print("Invalid input. Please enter a numeric value.")


while True:
    op = input("Press q to quit")
    if(op == "q"):
        break

    fillMatrix(A, b)
    solution = np.linalg.solve(A, b)
    print(solution)


