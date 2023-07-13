from multiprocessing import cpu_count, Pool
from time import sleep, time
from f import shunk_to_range, find_primes_mp_pool

#num_workers = cpu_count() - 1
num_workers = 16
num_end = 200000
num_shunks = 16

if __name__ == "__main__":
    tic = time()
    shunks = shunk_to_range(range(num_end), num_shunks)
    print("num_workers: {}".format(num_workers))
    pool = Pool(processes=num_workers)
    items = []
    for i, shunk in enumerate(shunks):
        items.append((
            shunk[0],
			shunk[-1]+1,
			i,
			1
        ))
    results = []
    for result in pool.starmap(func=find_primes_mp_pool, iterable=items):
        results.append(result)
    pool.close() # Wait until workers complete execution
    print(results)
    toc = time()
    print("Time elapsed: {}s".format(round(toc-tic)))
