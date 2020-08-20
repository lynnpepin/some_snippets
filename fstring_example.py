print(f"This is an fstring! 1/7 is approximately {1/7:.3f}.")
"""
>>> print(f"This is an fstring! 1/7 is approximately {1/7:.3f}.")
This is an fstring! 1/7 is approximately 0.143.
"""

print(f"This is ticket number {1025:>12}")
"""
>>> print(f"This is ticket number {1025:>12}")
This is ticket number         1025
# Note the whitespace 0123456789ab
# ":>12" right-justifies the number in a 12-character space
"""

print(f"Uh oh, I meant number {1025:>012}")
"""
>>> print(f"Uh oh, I meant number {1025:>012}")
Uh oh, I meant number 000000001025
# Same as above, but fills the space with zeros!
"""

def double(x):
    return 2*x

# New in Python 3.8: Self documentation with fstrings!
print(f"If you have 3.8, let's self document: {double(3) = }")
"""
>>> print(f"If you have 3.8, let's self document: {double(3) = }")
If you have 3.8, let's self document: double(3) = 6
# Noticee the fstring filled in the value!
"""
