

#using recursivity function 

def my_recurso(n):
    #Le cas de base qui cesse le processus et rassembler les résultats dispersés sous forme
    #d'une arbe 
    if(n==1): return 1;
    #Le processus en cours ; chaque applle a besoin de l'autre jusqu'à atteindre my_recurso(1) 
    else : return n+my_recurso(n-1)
# inviter l'utilisteur à fournir un nombre qu'il décrit à quel rang ,il veut la somme 

print("############################### start #################################")
m=int(input("ton nombre:"))

print("le resultat de votre nombre est :",my_recurso(m))

print("\n\n\n")
print("############################### End #################################")