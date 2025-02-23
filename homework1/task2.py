import pytest

def integer():
	x = 1
	y = 2
	out = x + y
	return out

def floaty():
	x = 1
	out = float(x)
	return out

def string():
	words = "Hello, World!"
	cut = words[:5]
	return cut

def boolean():
	x = 2
	y = 1
	gt = x > y
	return gt

def test_integer():
	assert integer() == 3

def test_floaty():
	assert floaty() == 1.0

def test_string():
	assert string() == "Hello"

def test_boolean():
	assert boolean() is True
	