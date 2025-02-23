import pytest

def count_words(fname):
    with open(fname, 'r')as file:
        words = file.read()
    return len(words.split())

true_count = 104

def gen_func_names(fname):
    def test_count_words():
        count = count_words(fname)
        print(f"required word count = true_count, found {count} for {fname}")
        assert count == true_count
    return test_count_words

text = ['task6_read_me.txt']

for file in text:
    test_name = 'test_' + file.replace('.','_')
    globals()[test_name] = gen_func_names(file)