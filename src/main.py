import sys 
import lru
import fifo

k = 3
requests = [1,2,3,4,5,1,2,3,1,2,3,4]

print("LRU  :", lru.lru(k, requests))
print("FIFO :", fifo.fifo(k, requests))
