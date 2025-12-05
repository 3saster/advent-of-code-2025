def parseData(lines):
    ranges = [[int(i) for i in l.split('-')] for l in lines[:lines.index('')]]
    IDs = [int(l) for l in lines[lines.index('')+1:]]
    return ranges,IDs

def Part1(ranges,IDs):
    valid = 0
    for id in IDs:
        for bot,top in ranges:
            if bot <= id <= top:
                valid += 1
                break
    return valid

# The main thing is to remove overlapping ranges
def Part2(ranges):
    L = len(ranges)
    for i in range( L ):
        j = 0
        while j < L:
            if i==j:
                j += 1
                continue
            reset = False
            if ranges[j][0] <= ranges[i][0] <= ranges[j][1]:
                ranges[i][0] = ranges[j][1] + 1
                reset = True
            if ranges[j][0] <= ranges[i][1] <= ranges[j][1]:
                ranges[i][1] = ranges[j][0] - 1
                reset = True
            j += 1
            if reset:
                j = 0
    
    valids = 0
    for bot,top in ranges:
        if (r:=top-bot+1) > 0:
            valids += r
    return valids

def Solution(lines):
    ranges,IDs = parseData(lines)
    yield Part1(ranges,IDs)
    yield Part2(ranges)