# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)

## Задание А — JSON ↔ CSV

Реализовал модуль `src/lab05/json_csv.py` с чистыми функциями `json_to_csv` и `csv_to_json`.
Функции не производят вывод в `stdout`, работают строго с кодировкой UTF-8 и валидируют входные данные.

### Функция json_to_csv:

```python
def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.

    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие
    поля пустыми строками. Порядок колонок формируется по ключам первого объекта
    с добавлением уникальных ключей из последующих записей.
    Кодировка строго UTF-8.

    Исключения:
        FileNotFoundError: Если входной файл не существует.
        ValueError: Если JSON пустой, содержит не словари или поврежден.
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

    if (
        not isinstance(data, list)
        or len(data) == 0
        or not all(isinstance(row, dict) for row in data)
    ):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

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

```

### Функция csv_to_json:

```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).

    Заголовок обязателен, значения сохраняются как строки.
    Запись выполняется с параметрами ensure_ascii=False, indent=2.
    Кодировка строго UTF-8.

    Исключения:
        FileNotFoundError: Если входной CSV-файл не существует.
        ValueError: Если файл пустой или не содержит строки заголовка.
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

```

### Пример работы:

```powershell
PS C:\Users\Admin\Desktop\python_labs> py -m src.lab05.json_csv
Конвертации JSON <-> CSV успешно выполнены.

```

**1. JSON → CSV (`data/samples/people.json` → `data/out/people_from_json.csv`):**

```csv
name,age,city
Alice,22,SPB
Bob,25,Moscow

```

**2. CSV → JSON (`data/samples/people.csv` → `data/out/people_from_csv.json`):**

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

**Примечание по структуре и типам данных:**

* Порядок колонок при формировании CSV строится по первому объекту, пропущенные поля дополняются пустой строкой `""` через `restval=""`.
* При чтении CSV все значения из `DictReader` поступают в виде строк, поэтому в выходном JSON числа остаются строковыми полями (`"age": "22"`),
что полностью соответствует специфике плоских CSV-таблиц.
* Запись JSON выполняется с `ensure_ascii=False` (для сохранения читаемой кириллицы) и `indent=2`.

---

## Задание Б — CSV → XLSX

Реализовал модуль `src/lab05/csv_xlsx.py` с функцией `csv_to_xlsx`, использующей библиотеку `openpyxl` (зафиксирована в `requirements.txt`).

### Функция csv_to_xlsx:

```python
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX с автоматической шириной колонок (не менее 8 символов).

    Первая строка таблицы переносится как заголовок.
    Имя листа по умолчанию — 'Sheet1'.
    Кодировка строго UTF-8.

    Исключения:
        FileNotFoundError: Если CSV-файл не найден.
        ValueError: Если файл пустой или не содержит строк.
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

    # Автоподбор ширины колонок по максимальной длине содержимого ячеек
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)

    p_out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(p_out)

```

### Пример работы:

```powershell
PS C:\Users\Admin\Desktop\python_labs> py -m src.lab05.csv_xlsx
Конвертация CSV -> XLSX успешно выполнена.

```

**Проверка сгенерированных таблиц (`people.xlsx`, `cities.xlsx`):**

* Лист таблицы корректно назван `Sheet1`.
* Данные выровнены, колонки не сжаты: ширина каждой колонки адаптирована под самый длинный текст с запасом `+3` символа (и не менее 8).

*(Сюда вставьте скриншот открытого в Excel/LibreOffice файла people.xlsx)*

`![Проверка XLSX](../../images/lab05/xlsx_check.png)`

---

## Краевые случаи и валидация

В соответствии с требованиями ТЗ обработаны следующие исключительные ситуации:

* **Файл отсутствует:** выбрасывается `FileNotFoundError` (не перехватывается молча, пути проверяются через `exists()`).
* **Пустой входной JSON / не список словарей:** выбрасывается `ValueError("Пустой JSON или неподдерживаемая структура")`.
* **Битый JSON-файл:** ошибка парсинга `json.JSONDecodeError` перехватывается и оборачивается в понятный `ValueError`.
* **Пустой CSV или файл без заголовков:** выбрасывается `ValueError("CSV без заголовка или пустой")`.

```

```