import random

def randomgenerator(size, seed=42):
    array=[]
    for i in range(size):
        array.append(random.randrange(size))
    return array
