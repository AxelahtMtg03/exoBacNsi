from math import sqrt   # import de la fonction racine carree

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = ...
    for i in range (1, len(tab)):
        if distance(tab[i], depart)< distance(point,depart):#
            point = tab[i]
            min_dist = ...
    return point
print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))
print( plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
print( plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))