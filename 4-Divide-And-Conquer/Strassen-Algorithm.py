import numpy as np

def matrix_addition(a, b):
    result = []
    length = len(a)
    for i in range(length):
        result.append([])
        for j in range(length):
            result[i].append(a[i][j] + b[i][j])
    return result


def matrix_subtract(a, b):
    result = []
    length = len(a)
    for i in range(length):
        result.append([])
        for j in range(length):
            result[i].append(a[i][j] - b[i][j])
    return result
    
def split(m):
    a = b = c = d = m
    while(len(a) > len(m)/2):
        a = a[:len(a)//2]
        b = b[:len(b)//2]
        c = c[len(c)//2:]
        d = d[len(d)//2:]
    while(len(a[0]) > len(m[0])/2):
        for i in range(len(a[0])//2):
            a[i] = a[i][:len(a[i])//2]
            b[i] = b[i][len(b[i])//2:]
            c[i] = c[i][:len(c[i])//2]
            d[i] = d[i][len(d[i])//2:]
    return a, b, c, d


def strassen(a, b, q):
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        a11, a12, a21, a22 = split(a)
        b11, b12, b21, b22 = split(b)

        p1 = strassen(matrix_addition(a11,a22), matrix_addition(b11,b22), q/2)
        p2 = strassen(matrix_addition(a21,a22), b11, q/2)
        p3 = strassen(a11, matrix_subtract(b12,b22), q/2)
        p4 = strassen(a22, matrix_subtract(b21,b11), q/2)
        p5 = strassen(matrix_addition(a11,a12), b22, q/2)
        p6 = strassen(matrix_subtract(a21,a11), matrix_addition(b11,b12), q/2)
        p7 = strassen(matrix_subtract(a12,a22), matrix_addition(b21,b22), q/2)

        c11 = matrix_addition(matrix_subtract(matrix_addition(p1, p4), p5), p7)
        c12 = matrix_addition(p3, p5)
        c21 = matrix_addition(p2, p4)
        c22 = matrix_addition(matrix_subtract(matrix_addition(p1, p3), p2), p6)

        c = np.zeros((len(c11)*2, len(c11)*2))
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j] = c11[i][j]
                c[i][j+len(c11)] = c12[i][j]
                c[i+len(c11)][j] = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c
   
def Problems():

    # problem 4.2-1
    A = [[1,3],[7,5]]
    B = [[6,8],[4,2]]
    
    print(strassen(A, B, len(A)))
        
Problems()