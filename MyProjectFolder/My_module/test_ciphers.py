from ciphers import *

def test_encode_message():
    
    assert callable(encode_message) # This tests that it is a function
    assert isinstance(encode_message('test'), str) # testing if output is correct type
    assert encode_message('abcde') == 'efghi' # testing for input and output