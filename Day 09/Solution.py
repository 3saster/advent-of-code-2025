from itertools import combinations

def between(n,a,b):
    return min(a,b) < n < max(a,b)
def betweenInc(n,a,b):
    return min(a,b) <= n <= max(a,b)

def inside(c,horEdges,vertEdges):
    for h1,h2 in horEdges:
        if c[1] == h1[1] and betweenInc(c[0],h1[0],h2[0]):
            return True
    # Raycasting algorithm
    crossings = 0
    for v1,v2 in vertEdges:
        if v1[0] >= c[0] and betweenInc(c[1],v1[1],v2[1]):
            crossings += 1
    return crossings%2 == 1


def parseData(lines):
    return [tuple(int(c) for c in l.split(',')) for l in lines]

def Part1(coord):
    area = 0
    for c1,c2 in combinations(coord,2):
        width  = abs(c1[0]-c2[0]) + 1
        height = abs(c1[1]-c2[1]) + 1
        if (a:=height*width) > area:
            area = a
    return area

def Part2(coord):
    area = 0
    horEdges  = []
    vertEdges = []
    # Deal with lines first
    for i in range( -1,len(coord)-1 ):
        c1,c2 = coord[i],coord[i+1]
        width  = abs(c1[0]-c2[0]) + 1
        height = abs(c1[1]-c2[1]) + 1
        if (a:=height*width) > area:
            area = a
        if c1[0] == c2[0]:
            vertEdges += [[c1,c2]]
        else:
            horEdges += [[c1,c2]]

    combos = list(combinations(coord,2))
    combos = sorted(combos,key=lambda c: -(abs(c[0][0]-c[1][0]) + 1)*(abs(c[0][1]-c[1][1]) + 1))
    for c1,c2 in combos:
        width  = abs(c1[0]-c2[0]) + 1
        height = abs(c1[1]-c2[1]) + 1
        if (a:=height*width) > area:
            breakOut = False
            # Nontrivial Rectangle lies inside polygon if
            # - No horizontal edges strictly inside the polygon
            if c1[0] > c2[0]: # Ensure c1 is left side corner
                c1,c2=c2,c1
            for v1,v2 in horEdges:
                if between(v1[1], c1[1],c2[1]):
                    if not (v1[0] <= c1[0] and v2[0] <= c1[0]) and not (v1[0] >= c2[0] and v2[0] >= c2[0]):
                        breakOut = True
                        break
            if breakOut: continue
            # - No vertical edges strictly inside the polygon
            if c1[1] > c2[1]: # Ensure c1 is top side corner
                c1,c2=c2,c1
            for v1,v2 in vertEdges:
                if between(v1[0], c1[0],c2[0]):
                    if not (v1[1] <= c1[1] and v2[1] <= c1[1]) and not (v1[1] >= c2[1] and v2[1] >= c2[1]):
                        breakOut = True
                        break
            if breakOut: continue
            # - All corners are inside the polygon
            if not (inside((c1[0],c2[1]),horEdges,vertEdges) and inside((c2[0],c1[1]),horEdges,vertEdges)):
                continue
            area = a
            break
        else:
            break
    return area

def Solution(lines):
    coord = parseData(lines)
    yield Part1(coord)
    yield Part2(coord)