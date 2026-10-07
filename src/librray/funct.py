def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''Функция возвращает минимум и максимум значений списка nums,
    который подается на вход.
    Если список пустой, то возвращает ValueError.
    '''
    if nums == []:
        raise ValueError #esli pustoy spisok
    minim, maxim = nums[0], nums[0]
    for el in nums:
        if el < minim:
            minim = el #nahodim min
        if el > maxim:
            maxim = el #nahodim maks
    return minim, maxim

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Функция сортирует поданый на вход список nums,
    возвращая уникальные значения в порядке возрастания.
    """
    uniq_nums = []
    for povt in nums:
        if povt not in uniq_nums:
            uniq_nums.append(povt) #уберу повторки (увидел в презе, что можно было просто сет заюзать...)

    for prohod in range(len(uniq_nums) - 1):
        for elem in range(len(uniq_nums) - 1 - prohod):
            if uniq_nums[elem] > uniq_nums[elem+1]:
                uniq_nums[elem], uniq_nums[elem+1] = uniq_nums[elem+1], uniq_nums[elem] #чисто бабл сорт

    return uniq_nums

def flatten(mat: list[list | tuple]) -> list:
    '''Функция превращает список списков/кортежей в один список по строкам (row-major).
    Если встречается строка/элемент, который не является списком/кортежем, то функция возвращает TypeError.
    '''
    # # for a in range(len(mat)):
    # #     if ((type(mat[a]) != list)) or (type(mat[a]) != tuple): raise TypeError #esle ne kortej or list
    for a in range(len(mat)):
        if isinstance(mat[a], str) or not isinstance(mat[a], (list, tuple)): raise TypeError('Элемент не явл. списком/кортежем') #проверка на тип
    
    itog_spis = []
    for i in range(len(mat)):
        for j in mat[i]:
            itog_spis.append(j)
            
    return itog_spis

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

def format_record(rec: tuple[str, str, float]) -> str:
    """Функция принимает на вход кортеж с ФИО, группой и gpa студента.
    Возвращается строка с ФИО, группой и gpa студента.
    Причем ФИО студента возвращается в виде "Фамилия И.О." или "Фамилия И.",
    инициалы формируются из 1–2 имён (в верхнем регистре), а лишние пробелы игнорируются;
    проверяется, чтобы gpa был в интервале от нуля до пяти включительно и печатался с 2 знаками.
    """
    fio, group, gpa = rec
    kuski = fio.split()
    surname = (kuski[0][0]).upper() + (kuski[0])[1:]
    init = ''.join((i[:1].upper() +'.' for i in kuski[1:]))

    if (gpa > 5) or (gpa < 0): raise ValueError('GPA должен быть в интервале от нуля до пяти вкключительно')
    znaki = f'{gpa:.2f}'

    return f'{surname} {init}, гр. {group}, GPA {znaki}'