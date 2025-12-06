from math import prod
import re

op = {'+':sum, '*':prod}
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def isInt(n: str):
    try:
        int(n)
        return True
    except:
        return False



def parseData(lines):
    operators = [op[o] for o in lines[-1].split()]
    rows = ["".join(nums) for nums in lines[:-1]]
    breakInd = [-1] + [i for i,s in enumerate(["".join(nums) for nums in transpose(rows)]) if re.match(r'^\s*$',s)]
    numbers = [ [r[i+1:j] for i,j in zip(breakInd, breakInd[1:]+[None])] for r in rows]
    return numbers,operators

def Part1(numbers,operators):
    total = 0
    newNumbers = [[int(n) for n in nums] for nums in transpose(numbers)]
    for row in range( len(newNumbers) ):
        total += operators[row]( newNumbers[row] )
    return total

def Part2(numbers,operators):
    total = 0
    newNumbers = [[int(num) for n in transpose(nums) if isInt(num:=''.join(n))] for nums in transpose(numbers)]
    for row in range( len(newNumbers) ):
        total += operators[row]( newNumbers[row] )
    return total

def Solution(lines):
    numbers,operators = parseData(lines)
    yield Part1(numbers,operators)
    yield Part2(numbers,operators)