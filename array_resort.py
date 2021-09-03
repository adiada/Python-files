#Q > Given a sorted array
# Eg : ip => -8 -3 0 4 6 9
    # sq => 64 9 0 16 36 81
    # op => 81 64 36 16 9 0 
import array as array

a = [-8,-3,0,4,6,9]


def squaresort(arr):
    n = len(arr)
    i = 0
    while(arr[i]!=0 and i < n):
        i = i + 1
    j = 0
    k = n - 1
    m = 0
    c = array.array('i',[])
    while( j < i and k > i):
        if(a[j] > a[k]):
            c = c.append(a[j])
            m = m + 1
            j = j + 1
        else:
            c = c.append(a[k])
            m = m + 1
            k = k - 1
    
    while(j < i):
        c[m] = a[j]
        m = m + 1
        k = k +1
    while(k > i):
        c[m] = a[k]
        m = m + 1 
        k = k - 1
    
    c[m] = 0
    return arr


squaresort(a)



