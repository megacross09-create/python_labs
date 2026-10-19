from src.library.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import sys
try:
    reading_text = read_text('data/lab04/input.txt')
except FileNotFoundError:
    print('Файл не существует')
    sys.exit(1)
normalized_text = normalize(reading_text)
tokenized_text = tokenize(normalized_text)
counted_text = count_freq(tokenized_text)
top-ned_text = top_n(counted_text)
# print(reading_text,'\n',normalized_text,'\n',tokenized_text,'\n',counted_text)

write_csv(counted_text, 'data/lab04/report.csv', header= ('word', 'count'))
N = sum(counted_text.values())
K = len(set(tokenized_text))
print(f'Всего слов: {N}\nУникальных слов: {K}\nТоп-5: {counted_text}')