def adjacent(grid,y,x):
    adj = 0
    for Y in [y-1,y,y+1]:
        for X in [x-1,x,x+1]:
            if (Y,X) in grid:
                adj += 1
    # Remove counting itself
    if (y,x) in grid:
        adj -= 1
    return adj
            

def Part1(papers):
    access = set()
    for p in papers:
        if adjacent(papers,p[0],p[1]) < 4:
            access.add(p)
    return len(access)

def Part2(papers):
    removed = 0
    access = True
    while access:
        access = set()
        for p in papers:
            if adjacent(papers,p[0],p[1]) < 4:
                access.add(p)
        for p in access:
            papers.remove(p)
        removed += len(access)
    return removed

def Solution(data):
    papers = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "@":
                papers.add( (y,x) )
    yield Part1(papers)
    yield Part2(papers)