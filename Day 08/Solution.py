def distSquared(A,B):
    dist = 0
    for a,b in zip(A,B):
        dist += (a-b)**2
    return dist

def parseData(lines):
    return [tuple(int(c) for c in l.split(',')) for l in lines]

def Part1(coord):
    pairs = 1000
    distances = []
    for i in range( len(coord) ):
        for j in range( i+1,len(coord) ):
            distances += [(coord[i],coord[j],distSquared(coord[i],coord[j]))]
    distances = sorted(distances,key=lambda x:x[2])
    pass

    junctionCircuits = dict()
    circuits = dict()

    maxcircuit = 0
    connections = 0
    for A,B,_ in distances:
        if A in junctionCircuits.keys() and B not in junctionCircuits.keys(): # One used
            circuits[junctionCircuits[A]].add(B)
            junctionCircuits[B] = junctionCircuits[A]
        elif B in junctionCircuits.keys() and A not in junctionCircuits.keys(): # One used
            circuits[junctionCircuits[B]].add(A)
            junctionCircuits[A] = junctionCircuits[B]
        elif A not in junctionCircuits.keys() and B not in junctionCircuits.keys(): # New circuit
            maxcircuit += 1
            circuits[maxcircuit] = {A,B}
            junctionCircuits[A] = maxcircuit
            junctionCircuits[B] = maxcircuit
        elif junctionCircuits[A] != junctionCircuits[B]: # Merge circuits
            oldCircuit = junctionCircuits[B]
            circuits[junctionCircuits[A]] |= circuits[oldCircuit]
            for junction in circuits[oldCircuit]:
                junctionCircuits[junction] = junctionCircuits[A]
            del circuits[oldCircuit]

        connections += 1
        if connections >= pairs:
            break
    largest = sorted(circuits.values(),key=lambda x:-len(x))[:3]
    return len(largest[0]) * len(largest[1]) * len(largest[2])

def Part2(coord):
    distances = []
    for i in range( len(coord) ):
        for j in range( i+1,len(coord) ):
            distances += [(coord[i],coord[j],distSquared(coord[i],coord[j]))]
    distances = sorted(distances,key=lambda x:x[2])
    pass

    junctionCircuits = dict()
    circuits = dict()

    maxcircuit = 0
    for A,B,_ in distances:
        if A in junctionCircuits.keys() and B not in junctionCircuits.keys(): # One used
            circuits[junctionCircuits[A]].add(B)
            junctionCircuits[B] = junctionCircuits[A]
        elif B in junctionCircuits.keys() and A not in junctionCircuits.keys(): # One used
            circuits[junctionCircuits[B]].add(A)
            junctionCircuits[A] = junctionCircuits[B]
        elif A not in junctionCircuits.keys() and B not in junctionCircuits.keys(): # New circuit
            maxcircuit += 1
            circuits[maxcircuit] = {A,B}
            junctionCircuits[A] = maxcircuit
            junctionCircuits[B] = maxcircuit
        elif junctionCircuits[A] != junctionCircuits[B]: # Merge circuits
            oldCircuit = junctionCircuits[B]
            circuits[junctionCircuits[A]] |= circuits[oldCircuit]
            for junction in circuits[oldCircuit]:
                junctionCircuits[junction] = junctionCircuits[A]
            del circuits[oldCircuit]

        # Everything is in one circuit
        if len(circuits.keys()) == 1 and len(list(circuits.values())[0]) == len(coord):
            return A[0] * B[0]

def Solution(lines):
    coord = parseData(lines)
    yield Part1(coord)
    yield Part2(coord)