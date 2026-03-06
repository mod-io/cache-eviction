import fifo
import sys
sys.path.insert(0, "../src")


#test 1
result = fifo.fifo(3, [1,2,3,1,4,2,3,4,1])
print("basic functionality:")
if result == 5:
    print("PASS")
else:
    print("FAIL")

#test 2
result = fifo.fifo(3, [1,2,3,1,2,3])
print("all hits")
if result == 3:
    print("PASS")
else:
    print("FAIL")

#test 3
result = fifo.fifo(1, [1,2,3,4])
print("all misses")
if result == 4:
    print("PASS")
else:
    print("FAIL")
