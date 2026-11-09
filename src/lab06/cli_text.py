import argparse
from pathlib import Path
import sys
from src.lab03.exA import tokenize, top_n, count_freq, normalize

def main():
    """
    Вывод содержимого с нумерацией строк (cat + флажок -n). Вывод частот слов (stats + --top n)
    В случае отсутствия файла - FileNotFoundError.
    """
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help='Входной файл в формате .txt')
    stats_parser.add_argument("--top", type=int, default=5, help='Частоты слов')

    args = parser.parse_args()


    if not args.command: #без подкоманд
        parser.print_help()
        return

    input_path = Path(args.input) 
    if not input_path.is_file(): raise FileNotFoundError(f'Файл не найден: {args.input}') #отсутсвие файла
    
    if args.command == "cat":
        """ Реализация команды cat """
        with open(input_path, 'r', encoding='utf-8') as f:
            for index, line in enumerate(f, start=1):
                clean_line = line.rstrip('\r\n') #cho-to ne to
                if args.n:
                    print(f'{index} {clean_line}')
                else:
                    print(clean_line)


    elif args.command == "stats":
        """ Реализация команды stats """
        if int(args.top) < 1:
            parser.error('Параметр --top должен быть положителен')

        text = input_path.read_text(encoding='utf-8')
        norm_text = normalize(text)
        token = tokenize(norm_text)
        freq = count_freq(token)
        N = sum(freq.values()) #or i could use 'len(token)' instead
        K = len(set(token)) #or i could use 'len(freq)' instead
        a = top_n(freq, n=int(args.top))

        print(f"Всего слов: {N}")
        print(f'Уникальных слов: {K}')
        print(f'Топ-{int(args.top)}:')
        for w, c in a:
            print(f'{w}:{c}')




if __name__ == '__main__':
    main()