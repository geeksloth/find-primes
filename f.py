from os import getpid


def is_prime(val):
	if val == 1:
		return False
	elif val > 1:
		for i in range(2, val):
			if (val % i) == 0:
				return False
		else:
			return True

def find_primes(begin, end, step=1):
	found = 0
	for i in range(begin, end, step):
		if is_prime(i):
			found += 1
	print(found)

def find_primes_mp(begin, end, return_dict, process_name, step=1):
	found = 0
	for i in range(begin, end, step):
		if is_prime(i):
			found += 1
	#print(found)
	return_dict[process_name]=found

def find_primes_mp_pool(begin, end, process_name, step=1):
	found = 0
	for i in range(begin, end, step):
		if is_prime(i):
			found += 1
	print((getpid(), process_name, found))
	return (process_name, found)

def shunk_to_range(seq, part):
	'''
	usage: 
	shunks = shunk_to_range(range(whole), num_of_parts)
	for shunk in shunks:
		print(shunk)
		for i in shunk:
			print(i)
	'''
	avg = len(seq) / float(part)
	out = []
	last = 0.0
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	return out