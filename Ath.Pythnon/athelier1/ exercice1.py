
# La définition de la fonction assistante en utilisant la récursivité 
def fact(i):
    if(i==0):return 1
    else : return i*fact(i-1)

# La définition de la fonction principale 
def sum(n):
    coun=0
    for s in range(1,n+1):
        coun+=fact(s)/s
    return coun 

# Invitation de l'utilisateur à fournir le rang 
print("***************** La sorie *************************")
yourNumber=int(input("taper votre rang à calculer :"))

# Affichage du résultat finale 
print("votre résultat est :",sum(yourNumber))
print("**************** Fin ***********************************")