q = str(input())
print(f'Инициалы: {(''.join([i[:1] for i in q.split()])).upper()}.\nДлина (символов): {' '.join(q.split()).count('')-1}')
# надо трайнуть генератором иницаилы вырезат и всес