a,b=map(int,input().split())
for i in range(a,b+1):
    div=[] #divisers
    countd=0
    for j in range(1,i//2+1):
        if i%j==0:
            countd+=1
            div.append(j)
    if countd==3:
        print(i)
        print(i,div[2],div[1],div[0])

