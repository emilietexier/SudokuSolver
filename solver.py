# valeur 0 dans la grille = case non remplie

#grille 1 = 36 cases sont donnees 

grille1 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

#grille 2 = 28 cases sont donnees

grille2 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 0, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 0, 5, 0, 0],
    [8, 2, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 0, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 0, 0, 0, 0]
]

# grille 3 = 17 cases sont donnees 

grille3 = [
    [0, 0, 0, 0, 6, 0, 0, 0, 1],
    [6, 8, 0, 0, 0, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 4, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 0, 4],
    [0, 4, 0, 0, 0, 0, 0, 0, 6],
    [7, 0, 0, 0, 1, 0, 0, 0, 0]
]

#grille 4 = 24 cases sont donnees

grille4 = [
    [0, 0, 0, 2, 0, 0, 7, 0, 1],
    [6, 8, 0, 0, 0, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 0, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 7, 4],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 0, 0, 0, 0]
]

#grille 5 = 22 cases sont donnees

grille5 = [
    [0, 0, 0, 2, 0, 0, 7, 0, 1],
    [6, 8, 0, 0, 0, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 0, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 6, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 0, 0, 0, 0]
]

#grille 6 = 20 cases sont donnees

grille6 = [
    [0, 0, 0, 2, 0, 0, 7, 0, 1],
    [6, 8, 0, 0, 0, 0, 0, 9, 0],
    [0, 9, 0, 0, 0, 0, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 6, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 8],
    [0, 0, 0, 3, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 3, 6],
    [7, 0, 0, 0, 1, 0, 0, 0, 0]
]

def remplir(grille, i, j):  # cette methode va nous donner les valeurs a remplir dans la grille = les cases vides
    for x in range(j, 9):
        for y in range(j, 9):
            if grille[x][y] == 0:
                return x,y
            
    for x in range(0, 9):
        for y in range(0, 9):
            if grille[x][y] == 0:
                return x,y
    return -1,-1



def isValid(grille, i, j, z):
    l = all([z != grille[i][x] for x in range(9)])
    if l:
        c = all([z != grille[x][j] for x in range(9)])
        if c:
            a, b = 3* (i//3), 3* (j//3)
            for x in range(a, b + 3):
                for y in range(a, b + 3):
                    if grille[x][y] == z:
                        return False
            return True
    return False 


def solveSudoku(grille, i=0, j=0):
        i,j = remplir(grille, i, j)
        if i == -1:
                return True
        for z in range(1,10):
                if isValid(grille,i,j,z):
                        grille[i][j] = z
                        if solveSudoku(grille, i, j):
                                return True
                        grille[i][j] = 0
        return False
   

solveSudoku(grille1)
print('NIVEAU FACILE')
print('36 cases donnees : ')
print(grille1)
print('NIVEAU MOYEN')
solveSudoku(grille2)
print('28 cases donnees : ')
print(grille2)
print('NIVEAU DIFFICILE')
solveSudoku(grille4)
print('24 cases donnees : ')
print(grille4)
solveSudoku(grille5)
print('22 cases donnees : ')
print(grille5)
#Les deux prochaines grilles sont tres lentes a calculer (niveau tres difficile du TP)
#Je les ai mises en commentaire pour avoir une execution tres rapide mais leurs resolutions fonctionnent
solveSudoku(grille6)
#print('20 cases donnees : ')
#print(grille6)
#solveSudoku(grille3)
#print('17 cases donnees : ')
#print(grille3)
