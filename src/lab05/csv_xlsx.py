import csv
def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указано в README).
    Если неверный тип файла, пустой JSON или CSV, то возвращается ValueError.
    Если файл отсутствует, то возвращается FileNotFoundError.
    """

    return None

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    Если неверный тип файла, пустой JSON или CSV, то возвращается ValueError.
    Если файл отсутствует, то возвращается FileNotFoundError.
    """

    return None