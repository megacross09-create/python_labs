from src.lab04.io_txt_csv import *
txt = read_text("data/lab04/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/lab04/check.csv")  # создаст CSV
print(txt)