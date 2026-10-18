from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''Читает текстовый файл и возвращает его содержимое (как одну строку).
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

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    # p = Path(path)
    # rows = list(rows)
    # first_len = len(rows[0])
    # if rows:
    #     if len(header) != first_len: raise ValueError('Файл некорректен (кол-во данных не совпадает с кол-вом колонок)')
    #     for r in rows:
    #         if len(r) != first_len: raise ValueError('Несовпадение длины строк. Все строки в rows должны иметь одинаковую длину')
    # with p.open("w", newline="", encoding="utf-8") as f:
    #     w = csv.writer(f)
    #     if header is not None:
    #         w.writerow(header)
    #     for r in rows:
    #         w.writerow(r)
    # return None
    '''ИЛИЛИЛИЛИЛ'''
    rows_list = list(rows)

    if rows_list:
        row_len = len(rows_list[0])
        if header is not None and len(header) != row_len:
            raise ValueError(
                f"Длина заголовка ({len(header)}) не совпадает с длиной строк ({row_len})"
            )
        for row in rows_list:
            if len(row) != row_len:
                raise ValueError("Все строки в rows должны иметь одинаковую длину")

    target_path = Path(path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with target_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)