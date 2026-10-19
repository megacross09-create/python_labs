from src.library.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys
try:
    reading_text = read_text('data/lab04/input_cp1251.txt')
except FileNotFoundError:
    print('Файл не существует')
    sys.exit(1)
    
normalized_text = normalize(reading_text)
tokenized_text = tokenize(normalized_text)
counted_text = count_freq(tokenized_text)
top_ned_text = top_n(counted_text, n=5)

sorted_rows = sorted(counted_text.items(), key = lambda p: (-p[1], p[0]))
write_csv(sorted_rows, 'data/lab04/report.csv', header= ('word', 'count'))

N = len(tokenized_text)
K = len(set(tokenized_text))

print(f'Всего слов: {N}\nУникальных слов: {K}\nТоп-5:')
for w, c in top_ned_text:
    print(f'{w}:{c}')