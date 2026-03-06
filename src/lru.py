def lru(k, requests):

    cache = []
    misses = 0

    for request in requests:

        if request in cache:
            cache.remove(request)
            cache.append(request)

        else:
            misses += 1

            if len(cache) == k:
                cache.pop(0)

            cache.append(request)
        
    return misses
