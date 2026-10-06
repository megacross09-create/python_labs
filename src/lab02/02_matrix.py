def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []: return []

    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица') #слишком долго обрабатвыает, стоит оптимизировать

    stroki = len(mat)
    stolby = len(mat[0])
    # for i in mat:
    #     if len(i) != stolby: raise ValueError('Рваная матрица') #вроде лучше

    new = [[mat[i][j] for i in range(stroki)] for j in range(stolby)]
    
    return new

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица')

    stroki = len(mat)
    # stolby = len(mat[0])
    summa = []
    for i in range(stroki):
         sloj = sum(mat[i])
         summa.append(sloj)
    return summa

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]: #жалк, что нельзя транспонир и сложить строки :((
    for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица')

    stroki = len(mat)
    stolby = len(mat[0])
    summa = [sum(mat[i][j] for i in range(stroki)) for j in range(stolby)]
    return summa

# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))

