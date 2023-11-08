# Nome: Código de complexidade 
# Descrição: Apresenta algumas análises de algoritmos simples 
# Autor: Luiz Augusto

import time
from collections import Counter
count = 0 # Global 


def timingl():
    probleme_size = 10000000
    print("%12s%16s" % ("Problem Size", "Seconds"))
    for i in range(5):
        start = time.time()
        work = 1
        for j in range(probleme_size):
            work += 1
            work -= 1
        elapsed = time.time() - start
        print("%12d%16.3f" % (probleme_size, elapsed))
        probleme_size *= 2

def timingl_1():
    probleme_size = 1000
    print("%12s%16s" % ("Problem Size", "Seconds"))
    for i in range(5):
        start = time.time()
        work = 1
        for j in range(probleme_size):
            for k in range(probleme_size):
                work += 1
                work -= 1
        elapsed = time.time() - start
        print("%12d%16.3f" % (probleme_size, elapsed))
        probleme_size *= 2

def counting():
    probleme_size = 1000
    print("%12s%16s" % ("Problem Size", "calls"))
    for i in range(5):
        number = 0
        work = 1
        for j in range(probleme_size):
            for k in range(probleme_size):
                number += 1
                work += 1
                work -= 1
        print("%12d%16d" % (probleme_size, number))
        probleme_size *= 2

def fib(n):
    global count
    count += 1
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def call_fib():
    global count

    probleme_size = 2
    print("%12s%15s" % ("Problem Size", "Calls"))
    for i in range(5):
        var = fib(probleme_size)
        print("%12d%15d"%(probleme_size,count))
        count = 0
        probleme_size*= 2

if __name__ == "__main__":
    #timingl()
    #timingl_1()
    #counting()
    call_fib()






