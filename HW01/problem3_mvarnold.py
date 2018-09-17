# STAT/CS 287
# HW 01
#
# Name: Michael Arnold
# Date: 09-12-18

import urllib.request
from string import punctuation


def words_of_book():
    """Download `A tale of two cities` from Project Gutenberg. Return a list of
    words. Punctuation has been removed and upper-case letters have been
    replaced with lower-case.
    """
    try:
        f = open("two_cities.txt")
        raw = f.read()
    except FileNotFoundError:

        # DOWNLOAD BOOK:
        url = "http://www.gutenberg.org/files/98/98.txt"
        req = urllib.request.urlopen(url)
        charset = req.headers.get_content_charset()
        raw = req.read().decode(charset)
        f = open('two_cities.txt', 'w')
        f.write(raw)
        f.close()
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
    """Count the words in the word list"""
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    sort_list = sorted(list(word_counts.items()), key = lambda x: x[1],reverse=True)
            
    return sort_list


print("word".ljust(10),"count".ljust(6))
print("-"*20)
words = words_of_book()
word_counts = count_most_common(words)
for word,count in word_counts[:100]:
    print(word.ljust(10),str(count).ljust(6))

