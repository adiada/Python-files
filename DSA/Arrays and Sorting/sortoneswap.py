#Sort an array in one swap whose two elements are swapped by mistake


def sortArray(A):

    sort1 = -1
    sort2 = -1

    for i in range(1,len(A)):
        if(A[i-1] > A[i]):
            if sort1 == -1:
                sort1 = i-1
                sort2 = i
            else:
                sort2 = i

    
    A[sort1], A[sort2] = A[sort2], A[sort1]


if __name__ == '__main__':

    A = [3,5,7,6,8,9]

    sortArray(A)

    print(A)

