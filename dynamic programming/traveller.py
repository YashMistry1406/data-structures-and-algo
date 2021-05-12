def gridTraveller(m,n,memory={}):
    key=str(m) +','+str(n)
    if key in memory:
        return memory[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0

    memory[key]=(gridTraveller(m-1,n,memory)+gridTraveller(m,n-1,memory))
    print(memory)
    return memory[key]
if __name__ == "__main__" :
    m,n=map(int,input().split())
    print(gridTraveller(m,n))

