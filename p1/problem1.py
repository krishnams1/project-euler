# Project Euler Problem 1 Solution usingPython
# Sum all numbers from 1 to 1000 that are divisible by 3 or 5

N = 1000

def sumMultFiveAndThree(maxnum):
    return reduce(lambda x,y: x+y, filter(lambda n:  (n%5 ==0) or (n%3 ==0),range(1,maxnum+1)))

print sumMultFiveAndThree(N)
