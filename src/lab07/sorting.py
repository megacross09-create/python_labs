def bubble_sort(nums) -> list:
    """
    Сортировка пузырьком.
    Возвращает новый список, отсортированный по возрастанию, исходный не меняется.
    """
    work = list(nums)
    for i in range(len(work)):
        was_swapped = False
        for j in range(len(work) - i - 1):
            if work[j] > work[j+1]:
                work[j], work[j+1] = work[j+1], work[j]
                was_swapped = True
        if was_swapped == False:
            break
    return work

def insertion_sort(nums) -> list:
    """
    Сортировка вставками.
    Возвращает новый список, отсортированный по возрастанию, исходный не меняется.
    """
    work = list(nums)
    for i in range(1, len(work)):
        key = work[i]
        j = i - 1
        while (j >= 0 and work[j] > key):
            work[j + 1] = work[j]
            j -= 1
        work[j + 1] = key
    return work

def selection_sort(nums) -> list:
    """
    Сортировка выбором.
    Возвращает новый список, отсортированный по возрастанию, исходный не меняется.
    """
    work = list(nums)
    for i in range(len(work)):
        min_indx = i
        for j in range(i + 1, len(work)):
            if work[j] < work[min_indx]:
                min_indx = j
        work[i], work[min_indx] = work[min_indx], work[i]
    return work