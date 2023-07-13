from time import time
from f import is_prime


num_end = 200000

tic = time()
found_all = 0
for i in range(num_end):
	if is_prime(i):
		found_all += 1
		#print(i)
toc = time()
print("Sequential, found_all: {}, elapse: {}s".format(found_all, round(toc-tic)))