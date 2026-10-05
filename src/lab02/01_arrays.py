def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if nums == []:
        raise ValueError #esli pustoy spisok
    minim, maxim = nums[0], nums[0]
    for el in nums:
        if el < minim:
            minim = el #nahodim min
        if el > maxim:
            maxim = el #nahodim maks
    return minim, maxim

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([]))
# print(min_max([1.5, 2, 2.0, -3.1]))



def unique_sorted(nums: list[float | int]) -> list[float | int]:
    uniq_nums = []
    for povt in nums:
        if povt not in uniq_nums:
            uniq_nums.append(povt) #уберу повторки (увидел в презе, что можно было просто сет заюзать...)

    for prohod in range(len(uniq_nums) - 1):
        for elem in range(len(uniq_nums) - 1 - prohod):
            if uniq_nums[elem] > uniq_nums[elem+1]:
                uniq_nums[elem], uniq_nums[elem+1] = uniq_nums[elem+1], uniq_nums[elem] #чисто бабл сорт

    return uniq_nums

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))



def flatten(mat: list[list | tuple]) -> list:
    # # for a in range(len(mat)):
    # #     if ((type(mat[a]) != list)) or (type(mat[a]) != tuple): raise TypeError #esle ne kortej or list
    for a in range(len(mat)):
        if isinstance(mat[a], str) or not isinstance(mat[a], (list, tuple)): raise TypeError('Элемент не явл. списком/кортежем') #проверка на тип
    
    itog_spis = []
    for i in range(len(mat)):
        for j in mat[i]:
            itog_spis.append(j)
            
    return itog_spis

# print(flatten([[1,2],[3,4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))

