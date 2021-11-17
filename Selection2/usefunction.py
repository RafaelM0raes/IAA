from functions import selection2
from randomnumbergenerator import randomgenerator
from time import time

size = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000]
for i in size:
    array = randomgenerator((i)*1000, seed=42)
    start = time()
    selection2(array, 10)
    print(f'{(i)*1000}, "{time()-start}"')
    
