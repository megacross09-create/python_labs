from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''Читает текстовый файл и возвращает его содержимое.
    По умолчанию используется кодировка'utf-8'.
    Если исходный файл сохранен в другой кодировке, укажите нужную явно
    (например, encoding="cp1251").
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)
# print(read_text('data/lab04/input.txt'))
# print(read_text('data/lab04/input1.txt'))
# print(read_text('data/lab04/input2.txt'))

import csv
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    from library.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))