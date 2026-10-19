# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание А
### Реализовал функции read_text, write_csv
Функция read_text:
```python
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
```
Пример работы:

![](../../images/lab04/test_case_A.png)

Функция write_csv:
```python
def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    #added strt
    if rows:
        first_len = len(rows[0])
        if header is not None and len(header) != first_len:
            raise ValueError("Длина header не совпадает с количеством колонок в rows")
        for r in rows:
            if len(r) != first_len:
                raise ValueError("Несовпадение длины строк. Все строки в rows должны иметь одинаковую длину")
    #added end
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
    return None
```
Пример работы:

![](../../images/lab04/test_case_csv.png)

## Задание B
### Написал скрипт, который читает текст(ы) из файлов, считает частоты и сохраняет отчёты. Если был пустой файл, то report.csv содержит только заголовок word, count
Один файл (база)
![](../../images/lab04/text_report.png)
Пустой файл
![](../../images/lab04/empty_file.png)
Кодировка cp1251
![](../../images/lab04/cp1251.png)