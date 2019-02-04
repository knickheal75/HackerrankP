a=[[[1,2,3],[0,9,2],[1,4,9]]]
b=[[[0,0,0],[0,0,0],[1,0,0]]]
c=[]

for i in range(1):
    newlists=[]
    for j in range(3):
        newlists1=[]
        for k in range(3):
            newlists1.append(a[i][j][k]+b[i][j][k])
        newlists.append(newlists1)
    c.append(newlists)  

print(c)


        