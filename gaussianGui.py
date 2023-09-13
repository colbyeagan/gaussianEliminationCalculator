import tkinter as tk
from tkinter import ttk

def gaussian_elimination_with_back_substitution(matrix):
    n = len(matrix)
    
    for col in range(n):
        # Find the pivot row
        pivot_row = None
        for i in range(col, n):
            if matrix[i][col] != 0:
                pivot_row = i
                break
        
        if pivot_row is None:
            return False  # Matrix cannot be converted to upper triangular form
        
        # Swap the current row with the pivot row
        matrix[col], matrix[pivot_row] = matrix[pivot_row], matrix[col]
        
        # Make the diagonal element 1
        pivot_element = matrix[col][col]
        for j in range(col, n + 1):  # Include the last column for the constants
            matrix[col][j] /= pivot_element
        
        # Eliminate other elements in the current column
        for i in range(col + 1, n):
            factor = matrix[i][col]
            for j in range(col, n + 1):  # Include the last column for the constants
                matrix[i][j] -= factor * matrix[col][j]
    
    # Back-substitution to find the solution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    
    return solution

def convert_to_upper_triangular(matrix):
    n = len(matrix)
    
    for col in range(n):
        # Find the pivot row
        pivot_row = None
        for i in range(col, n):
            if matrix[i][col] != 0:
                pivot_row = i
                break
        
        if pivot_row is None:
            return False, matrix  # Matrix cannot be converted to upper triangular form
        
        # Swap the current row with the pivot row
        matrix[col], matrix[pivot_row] = matrix[pivot_row], matrix[col]
        
        # Eliminate other elements in the current column
        pivot_element = matrix[col][col]
        for i in range(col + 1, n):
            factor = matrix[i][col] / pivot_element
            for j in range(col, n + 1):  # Include the last column for the constants
                matrix[i][j] -= factor * matrix[col][j]
    
    return True, matrix

def solve_equations():
    matrix = []
    for i in range(n):
        row = []
        for j in range(n + 1):
            entry = matrix_entries[i][j].get()
            if entry.strip() == "":
                entry = "0"
            row.append(round(float(entry), 2))  # Round input values to 2 decimal places
        matrix.append(row)

    success, result_matrix = convert_to_upper_triangular(matrix)
    if success:
        solution_label.config(text="Matrix in upper triangular form:")
        for i in range(n):
            solution_labels[i].config(text=" ".join(str(val) for val in result_matrix[i]))

        result = gaussian_elimination_with_back_substitution(result_matrix)
        if result:
            solution_label.config(text="Solution:")
            for i, val in enumerate(result):
                solution_labels[i + n].config(text=f'x{i + 1} = {val}')
    else:
        solution_label.config(text="No unique solution or matrix is inconsistent.")
        for i in range(n):
            solution_labels[i].config(text="")

# Create the main window
window = tk.Tk()
window.title("Gaussian Elimination Solver")

# Create input fields for matrix and constants
n = 3  # You can change this to match the desired matrix size
matrix_entries = [[None] * (n + 1) for _ in range(n)]

for i in range(n):
    for j in range(n + 1):
        entry = ttk.Entry(window)
        entry.grid(row=i, column=j, padx=5, pady=5)
        matrix_entries[i][j] = entry

# Create a Solve button
solve_button = ttk.Button(window, text="Solve", command=solve_equations)
solve_button.grid(row=n, column=n // 2, columnspan=2, padx=5, pady=10)

# Create a label to display the solution
solution_label = ttk.Label(window, text="")
solution_label.grid(row=n + 1, column=0, columnspan=n, padx=5, pady=5)

solution_labels = [ttk.Label(window, text="") for _ in range(n + n)]
for i in range(n + n):
    solution_labels[i].grid(row=n + 2 + i, column=0, columnspan=n, padx=5, pady=5)

window.mainloop()
