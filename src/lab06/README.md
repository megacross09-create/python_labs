# ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры): Техническое задание
## Задание cli_text
Содержит подкоманды stats, cat

### Подкоманда cat выводит содержимое текстового файла построчно. Для нумерации строк используется флаг -n.
Параметры:
--input — обязательный путь к входному файлу;
-n — необязательный флаг нумерации строк.

![](../../images/lab06/cli_text_cat.png)

### Подкоманда stats подсчитывает частоты слов в текстовом файле. Для обработки используются функции из src/library/text.py:
normalize() — нормализация текста;
tokenize() — выделение слов;
count_freq() — подсчёт частот;
top_n() — сортировка и выбор наиболее частых слов.

Параметры:
--input — обязательный путь к текстовому файлу;
--top — количество слов в результате (по дефолту 5).

![](../../images/lab06/cli_text_stats.png)


### --help
![](../../images/lab06/cli_text_help.png)


## Задание cli_convert
Содержит подкоманды json2csv, csv2json, csv2xlsx
### Что вводилось в терминал:
![](../../images/lab06/cli_terminal.png)
### Подкоманда json2csv преобразует JSON в CSV
![](../../images/lab06/people_json_sample.png)
![](../../images/lab06/people_csv_out.png)

### Подкоманда csv2json преобразует CSV в JSON
![](../../images/lab06/people_csv_sample.png)
![](../../images/lab06/people_json_out.png)

### Подкоманда csv2xlsx преобразует CSV в XLSX
![](../../images/lab06/cities_csv_sample.png)
![](../../images/lab06/cities_xlsx_out.png)
![](../../images/lab06/cli_convert_help.png)