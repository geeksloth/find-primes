from time import time
from threading import Thread
from multiprocessing import Manager
from f import shunk_to_range, find_primes_mp


num_workers = 4
num_end = 100000

if __name__ == "__main__":
	tic = time()
	manager = Manager()
	return_dict = manager.dict()
	workers = []
	shunks = shunk_to_range(range(num_end), num_workers)
	for i, shunk in enumerate(shunks):
		workers.append(Thread(target=find_primes_mp, args=[
			shunk[0],
			shunk[-1]+1,
			return_dict,
			i,
			1
			]))
	for p in workers:
		p.start()
	for p in workers:
		p.join()
	toc = time()
	print(return_dict)
	print("{} workers MP, elapse: {}s".format(num_workers, round(toc-tic)))