from textwrap import wrap

# Smallest s such that the string of s repeated rep times is greater than or equal n
def Greater(n,rep=2):
    n = str(n)
    L = len(n)
    if rep > L:
        return 0
    if L%rep != 0:
        out = 10**( L//rep )
    else:
        chunks = [int(s) for s in wrap(n, width=L//rep)]
        out = chunks[0]
        if int(str(out)*rep) < int(n) :
            out += 1
    return out

# Largest s such that the string of s repeated rep times is less than or equal n
def Lesser(n,rep=2):
    out = Greater(n,rep)
    if str(out)*rep == str(n):
        return out
    return out-1


def Part1(ranges):
    out = 0
    for first,second in ranges:
        maxRep = 2
        invalids = set()
        for rep in range(2,maxRep+1):
            for i in range(Greater(first,rep),Lesser(second,rep)+1):
                invalids.add( int(str(i)*rep) )
        out += sum(invalids)
    return out
        
def Part2(ranges):
    out = 0
    for first,second in ranges:
        maxRep = len(str(second))
        invalids = set()
        for rep in range(2,maxRep+1):
            for i in range(Greater(first,rep),Lesser(second,rep)+1):
                invalids.add( int(str(i)*rep) )
        out += sum(invalids)
    return out

def Solution(lines):
    ranges = [tuple(int(i) for i in r.split('-')) for r in lines[0].split(',')]
    yield Part1(ranges)
    yield Part2(ranges)