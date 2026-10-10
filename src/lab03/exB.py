from src.library.text import *
import sys

text = sys.stdin.read()
if text.strip() == "": raise ValueError("Введена пустая строка.")

N = normalize(text)
# K = 

print(f"Всего слов: {N}")
# print(f'Уникальных слов: {K}')
# print(f'Топ-5: {a}')