# Matrix_transpose
    ___transpose___
    The purpose of this fuction is educational
    It show in his code how a matrix transpose
    is done following the formal definition
    *NO LIST METHODS ALLOWED (.transpose(), .zip() etc...)*
    
    Formally, the transpose of a matrix A mxn is a A' matrix nxm
        - m (number of rows)
        - n (Number of colums)
    This means that the element[i][j] of A == element[j][i] of A'
    
    For e.g.:
    input: [
        [3, 5, 4, 3], 
        [6, 7, 5, 8], 
        [2, 1, 5, 0]
     ] 
    output: [
        [3, 6, 2],
        [5, 7, 1],
        [4, 5, 5],
        [3, 8, 0]
     ]
     Notice how new rows are the old columns and vice versa:
     A[i][j] == A'[j][i]
     
     For practical uses this fuction is USELESS
     There are more efficient methods to matrix tranpose.
     
     One of these methods is implemented on a fuction of
     the python package "numpy"
     Can be called as numpy.transpose();
     
     Another list usefull method than can matrix transpose is a
     default Python library fuction zip() or izip() from itertools.
