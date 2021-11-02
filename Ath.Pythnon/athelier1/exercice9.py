
 
def indixer(matrix,element):
    i=0
    N=len(matrix) # prévoir le nombre de ligne a l'aide de la focntion len()
    M=len(matrix[0]) #ici c'est le nombre de colonnes , puisqu'une marice donc tout le blocs
                    # ont même longueur 
    
    index=[-1,-1]
    while i<N:
    
        j=0   # on réintialiser à chaque itération de la boucle exterieur 
        while j<M:
            if matrix[i][j]== element : 
                index=[i+1,j+1]  # on ajoute 1 juste pour être compatible avec idxation ordinaire des ligne et colonne 
            j=j+1
            
        i=i+1
    return index  #renvoyer une liste de 2 élémnts : ligne  colonne ou bien -1 , -1 si l'elemen
                # n'est pas trouvalble 

matrix=[[6,7,8],[6,70,25],[-1,8,9]]
cheek=indixer(matrix,33)
print("################################### La sortie ######################################")
print("\n\n\n")
if  cheek[0] ==-1: # ce cas veut dire que on a taraversé toute la matrice sans trouver l'élement 
     print("l'élement n'est pas trouvable ")
else : 
    print("la position d'élement est ",cheek)
 