


 


list1=[22,33,14,56,79,88] # la première list 
list2=[-766,15,33,79,78,-9] # la deuxième list 

list3=[]  # la liste que sera remlpi à partir des précedentes 
i=0
while i < len(list1) :  # pour la longueur de la list 3 peut être déduit que ça soit à partir
                       #list1 ou la list2 
    if i%2==0 :
        list3.append(list1[i])
    else:
        list3.append(list2[i])
    i+=1 

print(list3)