from src.library.text import normalize
import sys

text = sys.stdin.readline() #mb should use input??
if text.strip() == "": raise ValueError("Введена пустая строка.")

N = normalize(text)
# K = 

print(f"Всего слов: {N}")
# print(f'Уникальных слов: {K}')
# print(f'Топ-5: {a}')