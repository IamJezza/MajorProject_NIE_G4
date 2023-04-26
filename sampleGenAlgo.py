
import random
random.seed(0) # set the seed

# function to find a solution
def func(x, y):
    return 8*x**3 - 4*x**2 - 9*y**3

# fitness function...
def fitness(x, y, val):
    return 1/abs(func(x, y)-val)

# to generate initial population
def population():
    s = []
    for i in range(100):
        s.append((random.uniform(-100, 100),
                  random.uniform(-100, 100)))
    return s

# initialization
pop = population()
print(pop)
val = 10
Count = 0

# forever loop...
while True:
    Count += 1
    bestresults = []
    for i in pop:
        bestresults.append((fitness(i[0], i[1], val), i))
    bestresults.sort(reverse=True)
    print("The best Solution of Gen = "+str(Count)+" is ")
    print(bestresults[0])
    print()
    if bestresults[0][0]>1000:
        break
    newGen = bestresults[:20]
    elements = []
    for i in newGen:
        elements.append(i[1][0])
        elements.append(i[1][1])
    newPop = []
    for i in range(50):
        newPop.append((random.choices(elements)[0]*random.uniform(0.99, 1.01), 
                       random.choices(elements)[0]*random.uniform(0.99, 1.01)))
    pop = newPop
