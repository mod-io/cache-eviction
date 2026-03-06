import sys 
import lru
import fifo

with open("../data/example1.in") as file:
    lines = file.readlines()

first_line = lines[0].split()
k = int (first_line[0])
m = int (first_line[1])

second_line = lines[1].split()
requests = []

for request in second_line:
    requests.append(int(request))

print("LRU  :", lru.lru(k, requests))
print("FIFO :", fifo.fifo(k, requests))
