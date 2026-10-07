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

# print([3, -1, 5, 5, 0], '->',min_max([3, -1, 5, 5, 0]))
# print([42], '->', min_max([42]))
# print([-5, -2, -9], '->', min_max([-5, -2, -9]))
# print([1.5, 2, 2.0, -3.1], '->', min_max([1.5, 2, 2.0, -3.1]))
# print([], '->', min_max([]))




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

# print([3, 1, 2, 1, 3], '->', unique_sorted([3, 1, 2, 1, 3]))
# print([], '->', unique_sorted([]))
# print([-1, -1, 0, 2, 2], '->', unique_sorted([-1, -1, 0, 2, 2]))
# print([1.0, 1, 2.5, 2.5, 0], '->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))



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

# print([[1,2],[3,4]], '->', flatten([[1,2],[3,4]]))
# print([[1, 2], (3, 4, 5)], '->', flatten([[1, 2], (3, 4, 5)]))
# print([[1], [], [2, 3]], '->', flatten([[1], [], [2, 3]]))
# print([[1, 2], "ab"], '->', flatten([[1, 2], "ab"]))

