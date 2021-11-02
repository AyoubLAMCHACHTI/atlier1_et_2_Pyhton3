


# fonction récursive à un seul parametre 
def fibo(n):
    if(n==0 or n== 1):
        return n 
    else : return fibo(n-2)+fibo(n-1)

print("############################### start #################################")
rang=int(input("taper le rang :"))
#Déclaration de la boucle while  
i=0
# appel multipe pour construire tous les termes 
while i<=rang :
    
    print(fibo(i),end=" ") # affichage des résultats fournit par la foction fib()
    i+=1                   # incrémenter la variable pour construire le terme suivant 
print("\n\n\n")
print("############################### End #################################")
