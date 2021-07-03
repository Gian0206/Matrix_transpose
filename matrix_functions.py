def transpose(matrix: list) -> list:
    """"
    ___transpose___
    The purpose of this fuction is educational
    It show in his code how a matrix transpose
    is done following the formal definition
    *NO LIST METHODS ALLOWED (.transpose(), .zip() etc...)*
    
    For further documentatior check the REEDME.me
    in the repository folder
    """
    output = list() # The A' matrix
    new_row = list() # The new rows will be stored here
    for i in range(len(matrix[0])): # range(number of colums)
        for j in range(len(matrix)): # range(number of rows)
            new_row.append(matrix[j][i]) # The new row is the old column
        
        output.append(new_row) # The new row is finally put into the A' matrix
        new_row = [] # We clean the variable for the next iteration
    return output # Retrun of the A' matrix *OUTSIDE LOOP*
