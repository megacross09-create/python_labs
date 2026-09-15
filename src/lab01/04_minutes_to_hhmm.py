m = abs(int(input()))
h1 = m//60
h2 = m//60
if h1>24:
    h1 = h1%24
print(f'Минуты: {m}\n' f"{h1:02d}:{m-h2*60:02d}")