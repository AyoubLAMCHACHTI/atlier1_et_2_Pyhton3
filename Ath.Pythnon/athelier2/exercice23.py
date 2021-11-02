 


list=[20,13,12,44,78,99,9,99,12,13,12]
dic={}  # création d'une dictinnaire vide 

for i in list :
    dic[i]=list.count(i) # stocker le nombre d'occurence des élemnts de la list : 
                        # avec key: est l'element et value : c'est la fréquence de chaque elemnt 

# le nobre d'occurence est indiqué dans le dictionnaire 
print(dic)
    

