q = str(input("ФИО: "))
# print(f'Инициалы: {(''.join([i[:1] for i in q.split()])).upper()}.\nДлина (символов): {' '.join(q.split()).count('')-1}')
# # надо трайнуть генератором иницаилы вырезат и всес
init=(''.join([i[:1] for i in q.split()])).upper()
length = ' '.join(q.split()).count('')-1
print(f'Инициалы: {init}.\nДлина (символов): {length}')