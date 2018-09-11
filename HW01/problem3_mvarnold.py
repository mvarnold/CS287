# STAT/CS 287
# HW 01
#
# Name: <FILL ME IN>
# Date: <FILL ME IN>

import urllib.request
from string import punctuation


def words_of_book():
    """Download `A tale of two cities` from Project Gutenberg. Return a list of
    words. Punctuation has been removed and upper-case letters have been
    replaced with lower-case.
    """
    
    # DOWNLOAD BOOK:
    url = "http://www.gutenberg.org/files/98/98.txt"
    req = urllib.request.urlopen(url)
    charset = req.headers.get_content_charset()
    raw = req.read().decode(charset)
    
    # PARSE BOOK
    raw = raw[750:] # The first 750 or so characters are not part of the book.
    
    # Loop over every character in the string, keep it only if it is NOT
    # punctuation:
    exclude = set(punctuation) # Keep a set of "bad" characters.
    list_letters_noPunct = [ char for char in raw if char not in exclude ]
    
    # Now we have a list of LETTERS, *join* them back together to get words:
    text_noPunct = "".join(list_letters_noPunct)
    # (http://docs.python.org/3/library/stdtypes.html#str.join)
    
    # Split this big string into a list of words:
    list_words = text_noPunct.strip().split()
    
    # Convert to lower-case letters:
    list_words = [ word.lower() for word in list_words ]
    
    return list_words


def count_most_common(word_list):
    ### YOUR CODE HERE ###


### YOUR CODE HERE ###
