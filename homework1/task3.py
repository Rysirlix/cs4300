import pytest

def check_num(x):
	if x > 0:
		return "+"
	if x < 0:
		return "-"
	else:
		return "0"

def find_prime(x):
	if x <= 1:
		return False
	for i in range(2, int(x **0.5) + 1):
		if x % i == 0:
			return False
	return True

def prime_first_10():
	primes = []
	for x in range(2, 30):
		if find_prime(x):
			primes.append(x)
			if len(primes) == 10:
				break
	return primes

def sum_1_100():
	x = 1
	out = 0
	while x <= 100:
		out += x
		x +=1
	return out

def test_check_num():
	assert check_num(1) == "+"
	assert check_num(-1) == "-"
	assert check_num(0) == "0"

def test_prime_first_10():
	assert prime_first_10() == [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29]

def test_sum_1_100():
	assert sum_1_100() == 5050
