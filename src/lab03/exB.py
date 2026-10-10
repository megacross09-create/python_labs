import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
'''"python -m src.lab03.exB" (ввести в терминал,
    а потом через Ctrl+Z и Enter закончить(если винда, если нет, то Ctrl+D))'''

from src.library.text import *

text = sys.stdin.readline() #mb should use input??
if text.strip() == "": raise ValueError("Введена пустая строка.")
# text = "a a a a a a a Привет Привет Привет Привет Привет Привет qwe qwe qwe qwe qwe we we we we e e e r r i "
norm_text = normalize(text)
token = tokenize(norm_text)
freq = count_freq(token)

N = sum(freq.values())
K = len(set(token))
a = top_n(freq, n=5)

print(f"Всего слов: {N}")
print(f'Уникальных слов: {K}')
print('Топ-5:')
for w, c in a:
    print(f'{w}:{c}')