
#la focntion de tri par selctoion 
def Tri_par_selection (list ):
    tmp,i,j=0,0,0
    N=len(list)
    while i<N:
        j=i+1
        while j<N:
            if list[j] < list[i]:
                tmp=list[i]
                list[i]=list[j]
                list[j]=tmp
            j+=1
        i+=1
     
    return list 
list_a_trier=[1,-9,6,78,-99,41,0,-1111,-9999]
print(list_a_trier)

# la list sera trié 
list_a_trier=Tri_par_selection(list_a_trier)
print(list_a_trier)


