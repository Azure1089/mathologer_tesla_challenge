import math
file = open("./Source/tesla.data","r+")
mod = int(file.read(7)[-1:7])
mult = int(file.read(9)[-1:9])
file.close()
i=1
chain=[1]
while 1*(mult**i)%mod not in chain:
    chain.append(1*(mult**i)%mod)
    i+=1
chain.append(1)
print(chain)
for x in range(2,mod+1):
    if x not in chain:
        i=1
        if x != mod:
            chainx=[x]
        else:
            chainx=[0]
        while x*(mult**i)%mod not in chainx:
            chainx.append(x*(mult**i)%mod)
            i+=1
        if x != mod:
            chainx.append(x)
        else:
            chainx.append(0)
        for f in range(len(chainx)):
            chain.append(chainx[f])
        print(chainx)
        chainx=[]
        