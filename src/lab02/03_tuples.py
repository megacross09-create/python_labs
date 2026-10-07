def format_record(rec: tuple[str, str, float]) -> str:
    """Функция принимает на вход кортеж с ФИО, группой и gpa студента.
    Возвращается строка с ФИО, группой и gpa студента.
    Причем ФИО студента возвращается в виде "Фамилия И.О." или "Фамилия И.",
    инициалы формируются из 1–2 имён (в верхнем регистре), а лишние пробелы игнорируются;
    проверяется, чтобы gpa был в интервале от нуля до пяти включительно и печатался с 2 знаками.
    """
    if len(rec) != 3: raise ValueError('Количество элементов в кортеже неверно. Должно быть 3.')
    if not (type(rec[2]) is float): raise TypeError('Неверный тип данных.')
    if not type(rec) is tuple: raise TypeError("На вход получен не кортеж.")
    fio, group, gpa = rec
    kuski = fio.split()
    surname = (kuski[0][0]).upper() + (kuski[0])[1:]
    init = ''.join((i[:1].upper() +'.' for i in kuski[1:]))

    if (gpa > 5) or (gpa < 0): raise ValueError('GPA должен быть в интервале от нуля до пяти включительно')
    znaki = f'{gpa:.2f}'

    return f'{surname} {init}, гр. {group}, GPA {znaki}'

# print(("Иванов Иван Иванович", "BIVT-25", 4.6), '->', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# print(("Петров Пётр", "IKBO-12", 5.0), '->', format_record(("Петров Пётр", "IKBO-12", 5.0)))
# print(("Петров Пётр Петрович", "IKBO-12", 5.0), '->', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# print(("  сидорова  анна   сергеевна ", "ABB-01", 3.999), '->', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))




# init=(''.join([i[:1] for i in q.split()])).upper()
# fio = "иванов иван Иванович"
# kuski = fio.split()
# surname = (kuski[0][0]).upper() + (kuski[0])[1:]
# init = ''.join((i[:1].upper() +'.' for i in kuski[1:]))
# print(f'{surname} {init}')

# gpa = 0
# okr = f'{(round(gpa)):.2f}'
# print(okr)