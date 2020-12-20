def tokenizer(instring):
    """
    generator
    
    """
    
    # A note: This could be done recursively, but Python doesn't optimize tail
    # recursion.  Furthermore, this is a kind of 'ugly' way of tokenizing,
    # but I wanted to do it in a way that is both clear, and easy to
    # translate into other languages without relying on Python's wonderful
    # string manipulation tools. :)
    
    ii = 0
    jj = 0
    
    while jj < len(instring):
        # jj iterates over each character
        # ii 'stays behind' at the start of each token
        # tokens are split by spaces and parenthesis
        
        char = instring[jj]
        
        if char in '( )':               # split the token here!
            if not ii == jj:            # yield everything up until the split
                yield instring[ii:jj]
            
            if char in '()':         # we want to output parenthesis :)
                yield char
            
            ii = jj + 1                 # ii catches up with jj
        
        jj += 1

def tokenize(instring):
    return list(tokenizer(instring))
