import math
def maths():
    data=[]
    file = open("./Source/tesla.data","r+")
    x=file.readline()
    y=file.readline()
    mod = int(x[x.find(" ")+2:len(x)])
    mult = int(x[x.find(" ")+2:len(x)])
    file.close()
    i=1
    chain=[1]
    while 1*(mult**i)%mod not in chain:
        chain.append(1*(mult**i)%mod)
        i+=1
    chain.append(1)
    data.append(chain[0:len(chain)+1])
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
            data.append(chainx)
            chainx=[]
    return(data)
