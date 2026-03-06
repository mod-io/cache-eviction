from collections import deque

def fifo(k, requests):

    cache = set()
    misses = 0
    insertion_order = deque()

    for request in requests:

        if request in cache:
            continue

        else:
            misses += 1

            if len(cache) == k:
                oldest = insertion_order.popleft()
                cache.remove(oldest)

            cache.add(request)
            insertion_order.append(request)

    return misses        