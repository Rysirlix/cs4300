import pytest

def stringy():
	print("Hello, World!")

def test_stringy():
	stringy()
	cap = capsys.readouterr()
	
	assert cap.out == "Hello, World!\n"
