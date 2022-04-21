futuro=0
atual=1
anterior=0
lim = abs(int(input('How long may the sequence be: ')))
fiblist = []
for i in range(lim):
    fiblist.append(anterior)
    futuro=atual+anterior
    anterior=atual
    atual=futuro

print(fiblist)