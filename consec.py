a = [2,0,7,1,3,8,16]
n = len(a)
ht = {}
#Preprocessing:
for elem in a:
    ht[elem] = True

ans = 1

#Main code
for elem in a:
    if(elem -1 not in ht):
        print("Started counting from " + str(elem))
        cnt = 1
        for j in range(1,n):
            if(elem + j in ht):
                cnt += 1
            else:
                break
        if (cnt > ans):
            ans = cnt
    else:
        print("Ignoring " + str(elem))

print("Ans = " + str(ans))