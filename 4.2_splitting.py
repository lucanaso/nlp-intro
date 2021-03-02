# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 25 Jan 2021
# Contributors: empty for now
# URL: https://lucanaso.it/2021/02/03/splitting-nlp-di-base-in-python-4-di-9/
# License: GNU GPL v3.0, see the LICENSE file.
# Natural Language: blog post in Italian, code in English
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Step 4: Text-splitting
#


# ### Import section
import nltk
# nltk.download('brown')  # run only once
from nltk.corpus import brown  # totally 1.161.100 words
from NLP_base_library import text_splitting  # as ts
# import NLP_base_library  # as NLP

# ### Data Import
# read data from file
# filename = 'text_run_eng.txt'
# with open(filename, 'r') as reader:
#     input_raw_text = reader.read()
# Read the data from the Brown corpus
input_raw_text = ' '.join(brown.words()[:10000])  # only take the first 10k words


# set the parameters for splitting the text
words_in_chunk = 900

# split the input text, call our new function:
output = text_splitting(input_raw_text, words_in_chunk)
# output = ts(input_raw_text, words_in_chunk)
# output = NLP_base_library.text_splitting(input_raw_text, words_in_chunk)
# output = NLP.text_splitting(input_raw_text, words_in_chunk)

# print some general statistics
print('# General Statistics')
tot_chunk = len(output)
print('- The original text contains {} words'.format(len(input_raw_text.split(' '))))
print('- The desired chunk size is {} words'.format(words_in_chunk))
words_limit = 20
print('==>\n- The splitting function created {} chunks. Here they are:'.format(tot_chunk))
for i, chunk in zip(list(range(0, tot_chunk)), output):
    print('\tChunk n. {:2} ({} words) = {}'.format(i + 1, len(chunk.split(' ')), chunk[:20]))
