def linear_search(nums, x) -> int:
    """
    Линейный поиск.
    Поиск индекса первого вхождения, при отсутствии - "-1".
    """
    for i, j in enumerate(nums):
        if x == j: return i
    return -1


def binary_search(sorted_nums, x) -> int:
    """
    Бинарный поиск.
    Возвращает индекс любого вхождения x в отсортированном по возрастанию списке,
    при отсутствии элемента - '-1'.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] > x: hi = mid - 1
        else: lo = mid + 1
    return -1 

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Двойной цикл.
    Поиск пары индексов (i, j), i < j, таких что
    nums[i] + nums[j] == target, при отсутствии - None.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target-nums[i] == nums[j]: return (i, j)

    return None

        
def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    Цикл через словарь.
    Поиск пары индексов (i, j), i < j, таких что
    nums[i] + nums[j] == target, при отсутствии - None.
    """
    seen = {}
    for i, x  in enumerate(nums):
        need = target - x
        if need in seen: return seen[need], i
        seen[x] = i            
    return None