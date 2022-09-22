import sys
import math



#Borne limite du coordonnees X
min_x = 2 ** 30
max_x = -2 ** 30

#Initialisation d'une liste vide qui contiendra les coordonnees Y
coordonees_y = []

#Code fourni pas codingame
n = int(input("entre le nombre de maison"))
print ("nombre de maison est",n)
for i in range(n):
         x, y = [int(j) for j in input().split()]
######

# Ajoute les coordonnees Y des point à la liste 
         coordonees_y.append(y)  
         
#Calcul du coordonnees X minimum et maximum qui donne la longeur du cable horizontal
         if x < min_x:
            min_x = x
         if x > max_x: 
            max_x = x
taille_cable = max_x - min_x

# Triee les coordonnees Y du plus petit au plus grand
coordonees_y.sort()

#Determination de la mediane selon que nous avons un nombre paire ou impaire de maison
if  n%2 ==0:
    mediane1=coordonees_y[n // 2]
    mediane2=coordonees_y[n//2-1]
    y_median: int =(mediane1+mediane2)//2
else:
    y_median = coordonees_y[n // 2]

#Calcul de la longeur vertical selon la position de la mediane(distance separant la mediane des autres maison )
for y in coordonees_y:
        taille_cable+= abs(y_median - y)

print(taille_cable)
