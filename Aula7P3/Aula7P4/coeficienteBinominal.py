def fatorial (num):
    fat = 1
    for cont in range(1, num+1):
        fat = fat * cont
    return fat 

def binominal (n,k): 
    calcBinominal = fatorial(n)//(fatorial(k)*fatorial(n-k))
    return calcBinominal

print(binominal(4,2))
print(binominal(20,10))