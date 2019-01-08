"""
This program uses a function to generate a welcome string.
"""

def generate_greeting():
    """
    Return a standard greeting.

    TODO: Support Internationalization
    """
    return "Hello World!"

def test_generate_greeting():
    """
    Tests for the greeting generator.
    """
    assert generate_greeting() == "Hello World!"

if __name__=="__main__":
    print (generate_greeting())