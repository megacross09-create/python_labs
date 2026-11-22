import random
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> None:
    """
    Проверяет функцию сортировки на случайных списках против эталонной sorted().
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_search(trials: int = 100) -> None:
    """
    Проверяет linear_search и binary_search на случайных и крайних случаях.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)

        missing = 999
        try:
            nums.index(missing)
            assert False, f"Ожидался ValueError для {missing} в {nums}"
        except ValueError:
            pass

        assert (linear_search(nums, missing) == -1), f"linear_search ошиблась на отсутствующем {missing} в {nums}"
        assert (binary_search(sorted_nums, missing) == -1), f"binary_search ошиблась на отсутствующем {missing} в {sorted_nums}"

        if nums:
            targets = (random.choice(nums), sorted_nums[0], sorted_nums[-1])
            for x in targets:
                lin_idx = linear_search(nums, x)
                assert (lin_idx == nums.index(x)), f"linear_search ошиблась на {nums}, x={x}: {lin_idx}"

                bin_idx = binary_search(sorted_nums, x)
                assert (bin_idx != -1 and sorted_nums[bin_idx] == x), f"binary_search ошиблась на {sorted_nums}, x={x}: {bin_idx}"


def check_two_sum(trials: int = 100) -> None:
    """
    Сравнивает two_sum_brute и two_sum_fast на случайных списках.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        if n >= 2 and random.random() < 0.5:
            i1, i2 = random.sample(range(n), 2)
            target = nums[i1] + nums[i2]
        else:
            target = random.randint(-250, 250)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        if res_brute is None or res_fast is None:
            assert res_brute is None and res_fast is None, (f"Расхождение на {nums}, target={target}:" f"brute={res_brute}, fast={res_fast}")
        else:
            i_b, j_b = res_brute
            assert 0 <= i_b < j_b < len(nums) and nums[i_b] + nums[j_b] == target, (f"two_sum_brute вернула неверную пару {res_brute}" f"на {nums}, target={target}")

            i_f, j_f = res_fast
            assert 0 <= i_f < j_f < len(nums) and nums[i_f] + nums[j_f] == target, (f"two_sum_fast вернула неверную пару {res_fast} "f"на {nums}, target={target}")


if __name__ == "__main__":
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
        print(f"OK: {fn.__name__} (100 проверок)")

    check_search()
    print("OK: linear_search и binary_search (100 проверок)")

    check_two_sum()
    print("OK: two_sum_brute и two_sum_fast (100 проверок)")