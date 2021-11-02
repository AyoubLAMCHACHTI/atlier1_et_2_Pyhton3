#Definition de la foction récursive à un seul argument 
def compter(n): # n c'est le nombre à compter ses chiffres 
    if((n//10)==0): # le cas de base permet de renvoyer 1 qui montre que le nobmbre est constuit d'unité seulement 
        return 1
    else : return (1+ compter(n//10)) # ajouter un  à chaque appel different au cas de base 



print("############################################# start #########################################")
# inviter l'utilisateur et en même tmps conserver l'entré à la variable nombre 
nombre=int(input("le nombre est :"))
print("le resultat est :",compter(nombre)) # lui fournit le résultat 
print("############################################# end #########################################")

