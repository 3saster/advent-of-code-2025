def Part1(data):
    rotations = [int(d.replace("R","+").replace("L","-")) for d in data]
    dial = 50
    password = 0
    for r in rotations:
        dial = (dial+r) % 100
        if dial == 0:
            password += 1
    return password

def Part2(data):
    rotations = [int(d.replace("R","+").replace("L","-")) for d in data]
    dial = 50
    password = 0
    for r in rotations:
        # Flip things around
        if r < 0:
            dial = (100 - dial)%100

        password += (dial + abs(r))//100
        dial = (dial+abs(r)) % 100

        # Unflip things around
        if r < 0:
            dial = (100 - dial)%100
    return password

def Solution(lines):
    yield Part1(lines)
    yield Part2(lines)