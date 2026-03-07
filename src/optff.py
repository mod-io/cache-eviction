from collections import deque

def optff(k, requests):

    positions = {}
    for i, req in enumerate(requests):
        if req not in positions:
            positions[req] = deque()
        positions[req].append(i)

    cache = set()
    misses = 0

    for request in requests:
        
        positions[request].popleft()

        if request in cache:
            continue

        else:
            misses += 1

            if len(cache) == k:
                farthest_idx = float('-inf')
                evict_candidate = next(iter(cache))

                for item in cache:
                    item_positions = positions.get(item)
                    if not item_positions:
                        next_idx = float('inf')
                    else:
                        next_idx = float(item_positions[0])

                    if next_idx > farthest_idx:
                        farthest_idx = next_idx
                        evict_candidate = item

                cache.remove(evict_candidate)

            cache.add(request)

    return misses
