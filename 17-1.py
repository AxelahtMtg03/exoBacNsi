def moyenne(listeDeNotes:list)->int:
    a,b=0,0
    for i in range(len(listeDeNotes)):
        a+=listeDeNotes[i][0]*listeDeNotes[i][1]
        b+=listeDeNotes[i][1]
    return a/b
print(moyenne([(15, 2), (9, 1), (12, 3)]))