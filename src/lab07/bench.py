import timeit
from src.lab04.io_txt_csv import write_csv

import random
from collections.abc import Callable
from pathlib import Path

from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def repeater(fn: Callable[[], object], number: int = 1, repeat: int = 3) -> float:
    """
    Замеряет время одного вызова fn через timeit.repeat и возвращает минимум.
    """
    times = timeit.repeat(fn, number=number, repeat=repeat)
    return min(times) / number

############

def bench_sorts(n: int) -> list[tuple[str, int, str, float | str]]:
    """
    Замеряет sorted и три квадратичные сортировки на одном списке длины n.
    """
    nums = [random.randint(-100000, 100000) for _ in range(n)]
    rows: list[tuple[str, int, str, float | str]] = []

    sorted_runs = 20 if n <= 10000 else 5
    t_sorted = repeater(lambda: sorted(nums), number=sorted_runs, repeat=3)
    rows.append(("sort", n, "sorted", t_sorted))

    for fn in (bubble_sort, insertion_sort, selection_sort):
        if n >= 100000:
            rows.append(("sort", n, fn.__name__, "> 60 с"))
            continue

        runs = 3 if n <= 1000 else 1
        reps = 3 if n <= 1000 else 1
        t = repeater(lambda f=fn: f(nums), number=runs, repeat=reps)
        rows.append(("sort", n, fn.__name__, t))

    return rows

############

def bench_search(n: int = 100_000, num_queries: int = 10_000,) -> list[tuple[str, int, str, float]]:
    """
    Замеряет 10 000 запросов линейного и бинарного поиска по списку из 100 000 чисел.
    """
    nums = [random.randint(-100_000, 100_000) for _ in range(n)]
    queries = [random.randint(-100_000, 100_000) for _ in range(num_queries)]
    rows: list[tuple[str, int, str, float]] = []

    t_sort = repeater(lambda: sorted(nums), number=5, repeat=3)
    rows.append(("search", n, "sorting", t_sort))

    sorted_nums = sorted(nums)

    def run_linear() -> None:
        for x in queries:
            linear_search(nums, x)

    def run_binary() -> None:
        for x in queries:
            binary_search(sorted_nums, x)

    t_linear = repeater(run_linear, number=1, repeat=1)
    rows.append(("search", n, "linear_search", t_linear))

    t_binary = repeater(run_binary, number=5, repeat=3)
    rows.append(("search", n, "binary_search", t_binary))

    return rows

############

def bench_two_sum(n: int) -> list[tuple[str, int, str, float]]:
    """
    Замеряет two_sum_brute и two_sum_fast на списке длины n с гарантированной парой.
    """
    nums = [random.randint(-100_000, 100_000) for _ in range(n)]

    nums[-2] = 1_000_000
    nums[-1] = 1_000_001
    target = nums[-2] + nums[-1]

    rows: list[tuple[str, int, str, float]] = []

    brute_runs = 3 if n <= 1_000 else 1
    brute_reps = 3 if n <= 1_000 else 1
    t_brute = repeater(lambda: two_sum_brute(nums, target), number=brute_runs, repeat=brute_reps)
    rows.append(("two_sum", n, "two_sum_brute", t_brute))

    fast_runs = 100 if n <= 1_000 else 20
    t_fast = repeater(lambda: two_sum_fast(nums, target),number=fast_runs, repeat=3)
    rows.append(("two_sum", n, "two_sum_fast", t_fast))

    return rows

############

def format_seconds(value: float | str) -> str:
    """
    Форматирует числовое время до 6 знаков после запятой, строки оставляет как есть.
    """
    if isinstance(value, float):
        return f"{value:.6f}"
    return value


def main() -> None:
    random.seed(42)
    rows: list[tuple[str, int, str, float | str]] = []

    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n))

    rows.extend(bench_search())

    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))

    csv_path = Path("data/lab07/bench.csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    formatted_rows = [(task, n, impl, format_seconds(seconds)) for task, n, impl, seconds in rows]
    write_csv(formatted_rows, str(csv_path), header=("task", "n", "impl", "seconds"))

    print(f"{'task':<10} {'n':>8} {'impl':<18} {'seconds':>12}")
    print("-" * 51)
    for task, n, impl, seconds_text in formatted_rows:
        print(f"{task:<10} {n:>8} {impl:<18} {seconds_text:>12}")


if __name__ == "__main__":
    main()