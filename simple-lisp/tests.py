import unittest as ut
import numpy as np
from tokenizer import tokenize

class TokenizerTests(ut.TestCase):
    # All tests need to be run in a class
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    # Simple ways to do tests here
    # long digits, long functions, nested, three args
    def test_tokenizer_on_some_examples(self):
        self.assertEquals(tokenize('(+ 3 2)'), ['(','+','3','2',')'])
        
    def test_tokenizer_on_some_examples_with_long_digits(self):
        self.assertEquals(tokenize('(/ 100 314)'), ['(','/','100', '314',')'])
        
    def test_tokenizer_on_some_examples_with_negative(self):
        self.assertEquals(tokenize('(/ -3 2)'), ['(','/','-3','2',')'])
    
    def test_tokenizer_on_some_examples_with_many_arguments(self):
        self.assertEquals(tokenize('(* 1 2 3 4 5)'), ['(','*', '1', '2', '3', '4', '5', ')'])
    
    def test_tokenozer_on_nested_examples(self):
        self.assertEquals(tokenize('(* (+ 1 (/ 10 2) 3) (* 4 3))'),
            ['(','*','(','+','1','(','/','10','2',')','3',')','(','*','4','3',')',')'])
    
    def test_tokenizer_on_example_with_spaces(self):
        self.assertEquals(tokenize('   ( -   10   3    )'), ['(', '-', '10', '3', ')'])
        
    def test_tokenizer_on_example_with_long(self):
        self.assertEquals(tokenize('(hey whats up)'), ['(', 'hey', 'whats', 'up', ')']) 
    
    def test_tokenizer_with_decimals(self):
        self.assertEquals(tokenize('(+ 3 1.2)'), ['(', '+', '3', '1.2', ')'])
    
    def test_tokenizer_on_mixed_example(self):
        self.assertEquals(tokenize('(hey (+ 300 (* 4    -20.5 10)))'),
            ['(', 'hey', '(', '+', '300', '(', '*', '4', '-20.5', '10', ')', ')', ')'])


if __name__ == '__main__':
    # Run the tests
    ut.main(verbosity=2)

