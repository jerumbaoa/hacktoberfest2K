def merge(la,lb):
    (C,m,n)=([],len(la),len(lb))
    (i,j)=(0,0)
    while ( i+j < m+n ):
        if i==m :
            #C.append(lb[j])
            j=j+1
        elif j==n :
            C.append(la[i])
            i=i+1
        elif la[i]<lb[j]:
            C.append(la[i])
            i=i+1
        elif la[i]>lb[j]:
            #C.append(lb[j])
            j=j+1
        elif la[i]==lb[j]:
            i=i+1
            j=j+1
    return C

def mergesort(l,left,right):
    if right-left <= 1 :
        return(l[left:right])
    if right-left > 1 :
        mid=(right+left)//2
        L=mergesort(l,left,mid)
        R=mergesort(l,mid,right)
        return merge(L,R)

l=[10,10,12,14,9,8,13]
print(mergesort(l,0,len(l)))
 
