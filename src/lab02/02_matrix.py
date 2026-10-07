def transpose(mat: list[list[float | int]]) -> list[list]:
    """Функция транспонирует поданую на вход матрицу mat.
    Если на вход была подана пустая матрица
    или строки поданой матрицы разной длины,
    то возвращается пустая матрица или ValueError соответственно.
    """
    if mat == []: return []

    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица') #слишком долго обрабатвыает, стоит оптимизировать

    stroki = len(mat)
    stolby = len(mat[0])
    # for i in mat:
    #     if len(i) != stolby: raise ValueError('Рваная матрица') #вроде лучше

    new = [[mat[i][j] for i in range(stroki)] for j in range(stolby)]
    
    return new

# print([[1, 2, 3]], '->', transpose([[1, 2, 3]]))
# print([[1], [2], [3]], '->', transpose([[1], [2], [3]]))
# print([[1, 2], [3, 4]], '->', transpose([[1, 2], [3, 4]]))
# print([], '->', transpose([]))
# print([[1, 2], [3]], '->', transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Функции подается на вход матрица mat, чьи строки суммируются.
    Если на вход была подана матрица, чьи строки разной длины,
    то функция возвращает ValueError.
    """
    for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица')

    stroki = len(mat)
    # stolby = len(mat[0])
    summa = []
    for i in range(stroki):
         sloj = sum(mat[i])
         summa.append(sloj)
    return summa

# print([[1, 2, 3], [4, 5, 6]], '->', row_sums([[1, 2, 3], [4, 5, 6]]))
# print([[-1, 1], [10, -10]], '->', row_sums([[-1, 1], [10, -10]]))
# print([[0, 0], [0, 0]], '->', row_sums([[0, 0], [0, 0]]))
# print([[1, 2], [3]], '->', row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]: #жалк, что нельзя транспонир и сложить строки :((
    """Функции подается на вход матрица mat, чьи столбцы суммируются.
    Если на вход была подана матрица, чьи строки разной длины,
    то функция возвращает ValueError.
    """
    for i in range(len(mat) - 1):
            if len(mat[i]) != len(mat[i+1]): raise ValueError('Рваная матрица')

    stroki = len(mat)
    stolby = len(mat[0])
    summa = [sum(mat[i][j] for i in range(stroki)) for j in range(stolby)]
    return summa

# print([[1, 2, 3], [4, 5, 6]], '->', col_sums([[1, 2, 3], [4, 5, 6]]))
# print([-1, 1], [10, -10], '->', col_sums([[-1, 1], [10, -10]]))
# print([[[0, 0], [0, 0]]], '->', col_sums([[0, 0], [0, 0]]))
# print([[1, 2], [3]], '->', col_sums([[1, 2], [3]]))

