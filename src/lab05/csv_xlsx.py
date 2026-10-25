def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    Если неверный тип файла, пустой JSON или CSV, то возвращается ValueError.
    Если файл отсутствует, то возвращается FileNotFoundError' 
    """