# Pick the largest digit that isn't the last, then pick the next largest digit
def joltage(bank,on):
    if on == 1:
        return int( max(bank) )
    else:
        ind, d = max(enumerate(bank[:-on+1]), key=lambda x: x[1])
        return int( d+str( joltage(bank[ind+1:],on-1) ) )

def Part1(data):
    return sum( joltage(bank,2) for bank in data )

def Part2(data):
    return sum( joltage(bank,12) for bank in data )

def Solution(lines):
    yield Part1(lines)
    yield Part2(lines)