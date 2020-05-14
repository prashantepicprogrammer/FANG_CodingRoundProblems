
""" Reshaping a matrix means to take the same elements in a matrix but change the row and column length . This means that the new 
    matrix needs to have the same elements filled in the same row order as the old matrix. Given a matrix, a new row size x and a 
    new column size y , reshape the matrix . If it is not possible to reshape , return None . 

    ex: input --> reshape_matrix([[1, 2], [3, 4]] , 1, 4)
        output --> [[1], [2], [3], [4]]

"""

def reshape_matrix(mat,x,y):
    rowInMat = mat.__len__()
    colInMat = mat[0].__len__()
    if rowInMat*colInMat != x*y:
        return None
    else :
        result = [[0 for i in range(x)] for j in range(y)]
        i=j=0
        for row in range(rowInMat):
            for col in range(colInMat):
                result[i][j] = mat[row][col]
                j=j+1

                if j >= x :
                    i = i + 1
                    j = 0
        return result        

print(reshape_matrix([[1,2], [3,4]] , 2,4))