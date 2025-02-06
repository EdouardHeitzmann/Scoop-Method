#Toy example
#Generate nodes
M_7 = 158753814 #This is the known size of the 7x7 grid metagraph
nodes = []
for i in range(M_7):
    nodes.append((random.random(),random.random()))
print(nodes[0])

#This next bit mimics the main chain
past = set()
L_times = []
#pick r so that a euclidean ball of radius r contains 6*10**(-6) of the area in [0,1]x[0,1]
r = (6*10**(-6)/math.pi)**(1/2)
for j in range(20000):
    new_node = random.choice(nodes)
    for old_node in past:
        if (new_node[0]-old_node[0])**2 + (new_node[1]-old_node[1])**2 < r**2:
            L_times.append(len(past)+1)
            past = set()
            break
    past.add(new_node)
average_L=sum(L_times)/len(L_times)
print(average_L)

#This next bit is how you would estimate M from a known value of L
def expected_T(N,M):
    factor = float(N/M)
    expectation = 0
    for t in range(math.ceil(M/N)):
        expectation+=factor*(t**2+t)
        factor*=(M-t*N)/M
    return(expectation)

def seek_M(L,N):
    b = 2**int(math.log(L,2)+1)
    overshot = 0
    while not overshot:
        if expected_T(N,b)>L:
            overshot = 1
        else: 
            b*=2
    a = int(b/2)
    while b-a !=1:
        c= (b+a)/2
        if expected_T(N,c)>L:
            b=int(c)
        else:
            a=int(c)
    if expected_T(N,a)-L>L-expected_T(N,b) :
        return b
    else:
        return a

print((seek_M(average_L,6*10**(-6)*M_7)-M_7)/M_7) #This gives us the % error of our estimate of M.
