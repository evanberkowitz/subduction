import numpy

def indices(mat):
    sets=[[0]]
    for row in range(len(mat)):
        for col in range(len(mat[0,:])):
            included=False
            if( mat[row,col] == 0):
                continue
            for s in sets:
                if(row in s and col not in s):
                    s+=[col]
                    included=True
                if(row not in s and col in s):
                    s+=[row]
                    included=True
                if(row in s and col in s):
                    included=True
            if( not included ):
                if( row == col):
                    sets += [[row]]
                else: sets += [[row, col]]
    return sets