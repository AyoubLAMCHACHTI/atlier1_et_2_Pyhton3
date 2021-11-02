

#definition de la fonction récursive permittant de passer du décimzl à binaire 

def DecimalTobinary(number):
    
    if(number//2 != 0):
        DecimalTobinary(number//2)
    print(number%2,end='')



#si vous permettez j'aimerais bien d'utliser quelques instructions de plus , juste pour isoler l'affichage
#  dans le terminal
print("##################### début du programme ##########################")
 # donner l'utilisateur lapossibilité de saisir un nombre 
 
usernumber=int(input("entrer un nombre :"))

#On veut bien de prévoir que l'utilisateur a enté un nombre entier mais avec la fonction 
#input il y'a le fait qu'elle envoie ce qui a fournit l'utilisateur comme un string 
#Même qu'on peut le  transformer avant de l'affecter à la variable , ça sert à rien s'il s'agit 
# D'un caractère 
 
# pour ce là ,on suppose que l'utilisateur va fournir un nombre un entier , sinon va s'afficher une erreur 

print(usernumber,"en bainaire ",end='')
DecimalTobinary(usernumber)

print("\n\n\n")
print("####################### La fin #####################################")
 


