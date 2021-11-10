from functions import quicksort
from randomnumbergenerator import randomgenerator
from time import time
from sys import argv

size = int(argv[1])

array = randomgenerator(size, seed=42)

startTime = time()
quicksort(array)
print(array[int(argv[2])])
print(f"total time: {time()-startTime}")
