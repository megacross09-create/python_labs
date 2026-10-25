# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)


## Описание работы

Реализованы модули для двусторонней конвертации данных между форматами JSON, CSV и XLSX. Функции являются «чистыми»
— не производят вывод в `stdout`, работают исключительно с файловой системой и валидируют входные данные.

---

## Зависимости

Для работы с форматом XLSX используется библиотека `openpyxl`. Все остальные используемые модули (`json`, `csv`, `pathlib`)
входят в стандартную библиотеку Python.

Установка зависимостей из корня репозитория:

```bash
pip install -r requirements.txt

```

Содержимое `requirements.txt`:

```text
openpyxl==3.1.5

```

---

## Задание А — JSON ↔ CSV

Реализован модуль `src/lab05/json_csv.py` с функциями `json_to_csv` и `csv_to_json`.

### Особенности реализации и допущения:

1. **Порядок колонок (JSON → CSV):** формируется на основе порядка ключей первого объекта с добавлением уникальных ключей из последующих записей.


2. **Отсутствующие поля (JSON → CSV):** если у объекта отсутствует ключ, имеющийся в заголовке таблицы, поле заполняется пустой строкой `""` (через параметр `restval=""` в `csv.DictWriter`).


3. **Сохранение типов (CSV → JSON):** в соответствии с ТЗ и спецификой CSV (все данные читаются как текст), значения при экспорте в JSON сохраняются строками.


4. **Форматирование JSON:** запись выполняется с параметрами `ensure_ascii=False` (для сохранения читаемой кириллицы) и `indent=2` (для структурированного отступа).



### Исходный код `src/lab05/json_csv.py`:

```python
import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.

    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие
    поля пустыми строками. Порядок колонок формируется по первому объекту.
    Кодировка строго UTF-8.
    """
    p_in = Path(json_path)
    p_out = Path(csv_path)

    if not p_in.exists() or not p_in.is_file():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    try:
        with p_in.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as err:
        raise ValueError(f"Некорректный JSON-файл: {err.msg}") from err

    # Валидация структуры: непустой список словарей
    if (
        not isinstance(data, list)
        or len(data) == 0
        or not all(isinstance(row, dict) for row in data)
    ):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    # Сбор уникальных ключей с сохранением порядка первого объекта
    fieldnames: list[str] = []
    for row in data:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    p_out.parent.mkdir(parents=True, exist_ok=True)
    with p_out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).

    Заголовок обязателен, значения сохраняются как строки.
    Используется json.dump(..., ensure_ascii=False, indent=2).
    Кодировка строго UTF-8.
    """
    p_in = Path(csv_path)
    p_out = Path(json_path)

    if not p_in.exists() or not p_in.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with p_in.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV без заголовка или пустой")

        rows = list(reader)

    if not rows:
        raise ValueError("CSV без заголовка или пустой")

    p_out.parent.mkdir(parents=True, exist_ok=True)
    with p_out.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("Конвертации JSON <-> CSV успешно завершены.")

```

### Команда запуска:

```bash
python -m src.lab05.json_csv

```

---

## Задание Б — CSV → XLSX

Реализован модуль `src/lab05/csv_xlsx.py` с функцией `csv_to_xlsx`.

### Особенности реализации:

1. **Имя листа:** по умолчанию создаётся лист с именем `"Sheet1"`.


2. **Шапка таблицы:** первая строка CSV-файла переносится в качестве заголовка.


3. **Автоширина колонок:** вычисляется по формуле `max(длина_текста + 3, 8)`. Это предотвращает скрытие текста фильтрами ячеек Excel и удовлетворяет условию «не менее 8 символов».



### Исходный код `src/lab05/csv_xlsx.py`:

```python
import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX с автоматической шириной колонок (не менее 8 символов).

    Первая строка принимается за заголовок. Лист называется 'Sheet1'.
    Кодировка строго UTF-8.
    """
    p_in = Path(csv_path)
    p_out = Path(xlsx_path)

    if not p_in.exists() or not p_in.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with p_in.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV пустой или не содержит строк")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Расчет автоширины колонок по максимальной длине строки в ячейках
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)

    p_out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(p_out)


if __name__ == "__main__":
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    print("Конвертация CSV -> XLSX успешно завершена.")

```

### Команда запуска:

```bash
python -m src.lab05.csv_xlsx

```

---

## Сценарии демонстрации и проверка результатов

### Сценарий 1: JSON → CSV

* **Входные данные (`data/samples/people.json`):**



```json
[
  {"name": "Alice", "age": 22, "city": "SPB"},
  {"name": "Bob", "age": 25, "city": "Moscow"}
]

```

* **Результат (`data/out/people_from_json.csv`):**



```csv
name,age,city
Alice,22,SPB
Bob,25,Moscow

```

* **Проверка:** Заголовок сохранён, порядок колонок соответствует полям объектов, количество строк совпадает с количеством элементов списка.



### Сценарий 2: CSV → JSON

* **Входные данные (`data/samples/people.csv`):**



```csv
name,age,city
Alice,22,SPB
Bob,25,Moscow

```

* **Результат (`data/out/people_from_csv.json`):**



```json
[
  {
    "name": "Alice",
    "age": "22",
    "city": "SPB"
  },
  {
    "name": "Bob",
    "age": "25",
    "city": "Moscow"
  }
]

```

* **Проверка:** Ключи объектов соответствуют заголовку CSV, значения сохранены строками, число объектов равно числу строк данных в CSV.



### Сценарий 3: CSV → XLSX

* **Входные данные:** `data/samples/people.csv` и `data/samples/cities.csv`.


* **Результат:** `data/out/people.xlsx` и `data/out/cities.xlsx`.


* **Проверка структуры:** Файлы открываются без ошибок в Excel / LibreOffice, активный лист имеет имя `"Sheet1"`, ширина колонок адаптирована под длину текста содержимого.



*(Сюда прикрепите скриншот открытого Excel-файла)*
`![Проверка XLSX](../../images/lab05/xlsx_check.png)`

---

## Валидация и краевые случаи

В коде реализована обработка исключительных ситуаций согласно требованиям ТЗ:

* **Файл не существует:** генерируется исключение `FileNotFoundError`.


* **Пустой JSON / список с не-словарями / пустой CSV:** выбрасывается `ValueError("Пустой JSON или неподдерживаемая структура")` или `ValueError("CSV без заголовка или пустой")`.


* **Битый синтаксис JSON:** перехватывается `json.JSONDecodeError` и выбрасывается `ValueError` с описанием ошибки.