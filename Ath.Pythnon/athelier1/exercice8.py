
#frequecy of a caractere in a string 
def frequency(chaine , char ): # donction prendde argument l'un pour la chiane et l'autre
                               # pour le caractère à chercher sa frequence 
    c=0
    for i in chaine :
        if i==char:c+=1

    return c;

chaine=input("Ecrire une chaine :")
char=input("la caractere a chercher :")
print("la frequence ici est :",frequency(chaine,char))