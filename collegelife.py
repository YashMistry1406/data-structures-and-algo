for t in range(int(input())):


    n,m=map(int,input().split())
    f=list(map(int,input().split()))
    c=list(map(int,input().split()))
    mini=min(n,m)
    maxi=max(n,m)
    flag="f"
    count=0


    stack=[99999999999999999999999999999999999999999999]*maxi

    if n<m:
        f=f+stack
    else:
        c=c+stack


    for i in range(maxi):
        if i==0 and c[i]<f[i]:
            count+=1
            flag="c"

        if f[i]<c[i] and flag=="c":
            if f[i+1]>c[i]:
                count+=1
                flag="c"
            count+=1
            flag="f"
        if c[i]<f[i] and flag=="f":
            count+=1
            flag="f"

    print("count",count)
