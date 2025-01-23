import random
import time
from functools import lru_cache

def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])

def update_no_cache(array, index, value):
    array[index] = value

class CachedOperations:
    def __init__(self, array):
        self.array = array
        
    @lru_cache(maxsize=1000)
    def range_sum_with_cache(self, L, R):
        return sum(self.array[L:R + 1])
    
    def update_with_cache(self, index, value):
        self.array[index] = value
        self.range_sum_with_cache.cache_clear()

if __name__ == "__main__":
    N = 100_000
    Q = 50_000

    array = [random.randint(1, 1000) for _ in range(N)]
    queries = []
    for _ in range(Q):
        if random.choice([True, False]):
            L = random.randint(0, N - 1)
            R = random.randint(L, N - 1)
            queries.append(('Range', L, R))
        else:
            index = random.randint(0, N - 1)
            value = random.randint(1, 1000)
            queries.append(('Update', index, value))

    array_no_cache = array.copy()
    start_no_cache = time.time()
    for query in queries:
        if query[0] == 'Range':
            range_sum_no_cache(array_no_cache, query[1], query[2])
        else:
            update_no_cache(array_no_cache, query[1], query[2])
    end_no_cache = time.time()

    print(f"Час виконання без кешування: {end_no_cache - start_no_cache:.2f} секунд")

    array_with_cache = array.copy()
    cached_ops = CachedOperations(array_with_cache)
    start_with_cache = time.time()
    for query in queries:
        if query[0] == 'Range':
            cached_ops.range_sum_with_cache(query[1], query[2])
        else:
            cached_ops.update_with_cache(query[1], query[2])
    end_with_cache = time.time()

    print(f"Час виконання з LRU-кешем: {end_with_cache - start_with_cache:.2f} секунд")