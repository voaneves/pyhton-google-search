#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""google_search: search the 10 first results of a Google Search.
----------
    
    To do a google_search, you just have to execute this file, followed by the 
    search string as an argument.
        $ python google_search.py "string to be searched"
    Remember to run requirements.txt first.

TO DO
----------
    - Improve quality of results (titles, description, etc)
    - Implement saving to formatted external file
    - build requirements.txt file
    - improve the README.md
    - Publish to pip.
"""

import sys # to receive input
try:
    from googlesearch import search # try importing googlesearch
except ImportError:
    print("No module named 'google' found")

# function to convert a list into string
def convert(s): 
    string = "" 
    return(string.join(s)) 
        
# Assign the arguments passed to a variable search_string
search_string = sys.argv[1:]

# The argument passed to the program is accepted
# as list, it is needed to convert that into string
search_string = convert(search_string)
  
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+')

# Create a results string which will hold the results
results = []

# Use Google Search module to search all the results
for j in search(search_string, tld = "com", num = 10, stop = 10, pause = 2):
    results.append(j)