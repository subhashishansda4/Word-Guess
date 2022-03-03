# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:04:07 2022

@author: VAGUE
"""

# getting words through
# splitting a sentence into list of words
sent = ['this. is, the( (best) "place" on-earth_ _and: ;is the/ best']

words_0 = sent[0].split()

# storing all the symbols so that we can remove them
sym = ['.', ',', '(', ')', '"', '-', '_', ':', ';', '/']
for i in range(len(sym)):
    words_0 = [word.replace(sym[i], "") for word in words_0]
print(words_0)