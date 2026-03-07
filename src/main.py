import sys 
import lru
import fifo
import optff

files = ["../data/example1.in", 
         "../data/example2.in", 
         "../data/example3.in", 
         "../data/example4.in"]

for path in files:
    
    with open(path) as file:
        lines = file.readlines()

    first_line = lines[0].split()
    k = int (first_line[0])
    m = int (first_line[1])

    second_line = lines[1].split()
    requests = []

    for request in second_line:
        requests.append(int(request))

    print(path)
    print("LRU  :", lru.lru(k, requests))
    print("FIFO :", fifo.fifo(k, requests))
    print("OPTFF:", optff.optff(k, requests))
    print()