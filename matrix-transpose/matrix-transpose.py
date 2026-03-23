import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    arr = np.asarray(A, dtype = int)
    n_rows, n_cols = arr.shape
        
    A_T = np.zeros((n_cols, n_rows), dtype=int)
        
    for i in range(n_rows):
        for j in range(n_cols):
            A_T[j, i] = arr[i, j]
                
    return A_T