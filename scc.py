G = { }
for i in range(1, 875715) :
    G[i] = []

for l in open('SCC.txt','r').readlines():
    ins = []
    ins = l.split()
    x = int(ins[0])
    y = int(ins[1])
    G[x].append(y)
