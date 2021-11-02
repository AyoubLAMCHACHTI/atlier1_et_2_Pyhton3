

def cheek_value(dic,x): # cette fonction sert à prévoir l'existence d'une valeur dans le dictionnaire
    
    flag=-1   # la variable utiliser pour indiquer l'existence selon lsa valeur -1 
               # c'est à dire on a traversé le dic sans trouver l'elemnt chercher 
    for l in dic:
   
        if dic[l]==x :
            flag=0
            break
    if flag==0: return True
    else      : return False
        

list=[47, 64, 69, 37, 76, 83, 95, 97,11]
dic={'Yassine':47, 'Imane':69, 'Mohammed':11, 'Abir':97}

index=0
for x in list :
    
    if cheek_value(dic,x)==False: # la condition est vraie si la focntion return FALSE ; la valeur n'existe pas 
                                # dans ce cas on retirer l'elemnt de la liste 
        list.pop(index)
    index+=1

print(list)


 