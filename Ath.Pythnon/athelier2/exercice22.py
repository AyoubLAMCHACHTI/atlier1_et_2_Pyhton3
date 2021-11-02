list=[5,8,10,12,13,20,13,25,66]
i=0
while i < len(list) :
    list1=list[0:len(list)//3]   # prend le premier morceau
    list2=list[len(list)//3:2*(len(list)//3)] # le deuxième 
    list3=list[2*(len(list)//3):]               # le troisième 
    i+=1
# inverser le strois listes 
list1=list1[::-1]
list2=list2[::-1]
list3=list3[::-1]
print(" La liste primitive ",list)
print(" le trois listes générées(inversées):")
print(list1)
print(list2)
print(list3)

 