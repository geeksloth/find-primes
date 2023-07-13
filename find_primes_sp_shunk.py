from time import time
from f import is_prime, shunk_to_range


num_workers = 4
num_end = 100000

shunks = shunk_to_range(range(num_end), num_workers)
print(shunks)
found_all = 0
tic = time()
for shunk in shunks:
	found = 0
	print("worker {}'s finding.".format(shunk))

	for i in range(shunk[0], shunk[-1]+1):
		if is_prime(i):
			found += 1
	print(found)
	found_all += found

toc = time()

print("{} workers sequential, found_all: {}, elapse: {}s".format(num_workers, found_all, round(toc-tic)))