from collections import Counter, defaultdict

def parseData(lines):
    splitters = set()
    for y in range( len(lines) ):
        for x in range( len(lines[y]) ):
            if lines[y][x] == '^':
                splitters.add((y,x))
    
    for y in range( len(lines) ):
        for x in range( len(lines[y]) ):
            if lines[y][x] == 'S':
                return {(y,x)}, splitters

def Part1(beam,splitters):
    totalSplits = 0
    maxY = max(splitters,key=lambda s:s[0])[0]
    beamY = 1

    while beamY <= maxY:
        newBeams = set()
        rowSplitters = {s for s in splitters if s[0] == beamY}
        for y,x in beam:
            if (y+1,x) in rowSplitters:
                totalSplits += 1
                newBeams.add((y+1,x-1))
                newBeams.add((y+1,x+1))
            else:
                newBeams.add((y+1,x))
        beam = newBeams
        beamY += 1
    return totalSplits

def Part2(beam,splitters):
    maxY = max(splitters,key=lambda s:s[0])[0]
    beamY = 1
    beam = Counter(beam)

    while beamY <= maxY:
        newBeams = defaultdict(lambda: 0)
        rowSplitters = {s for s in splitters if s[0] == beamY}
        for y,x in beam.keys():
            if (y+1,x) in rowSplitters:
                newBeams[(y+1,x-1)] += beam[(y,x)]
                newBeams[(y+1,x+1)] += beam[(y,x)]
            else:
                newBeams[(y+1,x)] += beam[(y,x)]
        beam = newBeams
        beamY += 1
    return sum(beam.values())

def Solution(lines):
    beam,splitters = parseData(lines)
    yield Part1(beam,splitters)
    yield Part2(beam,splitters)