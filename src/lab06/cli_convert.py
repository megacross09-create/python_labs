import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    """
    Конвертация json в csv, csv в json, csv в xlsx.
    """
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("json2csv", help='Конвертация из json в csv формат')
    p1.add_argument("--in", dest="input", required=True, help='Файл json на вход')
    p1.add_argument("--out", dest="output", required=True, help='Файл csv на выход')

    p2 = sub.add_parser("csv2json", help='Конвертация из csv в json формат')
    p2.add_argument("--in", dest="input", required=True, help='Файл csv на вход')
    p2.add_argument("--out", dest="output", required=True, help='Файл json на выход')

    p3 = sub.add_parser("csv2xlsx", help='Конвертация из csv в xlsx формат')
    p3.add_argument("--in", dest="input", required=True, help='Файл csv на вход')
    p3.add_argument("--out", dest="output", required=True, help='Файл xlsx на выход')

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """


    if args.cmd == 'json2csv':
        json_to_csv(args.input, args.output)
    if args.cmd == 'csv2json':
        csv_to_json(args.input, args.output)
    if args.cmd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)

if __name__=='__main__':
    main()