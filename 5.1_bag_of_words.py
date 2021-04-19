# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 12 Mar 2021
# Contributors: empty for now
# URL: https://lucanaso.it/2021/03/21/bag-of-words-nlp-di-base-in-python-5-di-9/
# License: GNU GPL v3.0, see the LICENSE file.
# Natural Language: blog post in Italian, code in English
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Step 5: Bag of words
#


# ### Import section
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import brown  # totally 1.161.100 words, 57.340 sentences, 16.667 paragraphs
from NLP_base_library import text_splitting, print_dtm

# ###############
# PART 1: use a 1-doc corpus

# ### Data Import
# read data from file
filename = 'text_run_eng.txt'
with open(filename, 'r') as reader:
    input_raw_text = reader.read()
corpus = [input_raw_text]

# 1.1 Create Vocabulary
# Use the package scikit-learn (class CountVectorizer)
# Type "pip install scikit-learn" in the terminal to install the package
#   this will also download and install other important and common package such as numpy, scipy
#
# Create a CountVectorizer object named 'features'
features = CountVectorizer()
# can be personalised with several parameters (we keep it simple and use default)
# use the method "fit" to do the job
features.fit(corpus)
# 2 different ways to access the vocabulary
# - the method "get_feature_names" shows the vocabulary words (as a list)
# - the attribute "vocabulary_" stores the vocabulary (as a dictionary)
#       the key in the dictionary is the actual word
#       the value of the key is the word ID (integer)
vocabulary_words = features.get_feature_names()
print('Total amount of words found = {}\n'.format(len(vocabulary_words)))
print('Here is the corpus vocabulary as an ordered list:\n\t{}\n'.format(vocabulary_words))
print('Here is a python dictionary with the corpus vocabulary:\n\t{}\n'.format(features.vocabulary_))

# 1.2 Get the frequency
# Measure how often each feature (vocabulary word) is used in each corpus document (for Part 1 just 1 document)
# Use the "transform" method of the "features" object
#   the method returns a sparse matrix (--> use "toarray" to treat it as dense)
count_matrix = features.transform(corpus)
print('Here are the counts of each word (in order): \n\t{}\n'.format(count_matrix.toarray()))
print('Here is the matrix with the count of the words:\n{}\n'.format(count_matrix))
# let's print the results more nicely, e.g. word - count
print('Word\t--\tCount')
for word, count in zip(vocabulary_words, count_matrix.toarray()[0]):
    print('{}\t--\t{}'.format(word, count))
print('')

# 1.3 fit & transform
# Method "fit_transform"
# "is equivalent to fit followed by transform, but more efficiently implemented."
ft_test = CountVectorizer()
ft_count_matrix = ft_test.fit_transform(corpus)
print('Here is the corpus vocabulary obtained with the "fit_transform" method:\n\t{}\n'.
      format(ft_test.get_feature_names()))

# ###############
# PART 2: use a 10-doc corpus
# Now let's do the same as for Part 1, but for a corpus with several documents

# 2.1 Build the corpus
#   2.1.1
#   Get the words from the brown dataset (already in NLTK) and join them together into a single document
input_raw_text = ' '.join(brown.words()[:10000])  # take the first 10k words (out of about 1M)
#   2.1.2
#   Split the single document into chunks (using the function we built in previous article)
#   and consider each chunk as a separate document
doc_size = 1000  # Number of words in each chunk
my_corpus = text_splitting(input_raw_text, doc_size)  # this returns a list, each list is one chunk

# 2.2 Get the vocabulary and the word count (Bag of words)
features2 = CountVectorizer()
count_matrix2 = features2.fit_transform(my_corpus)
# Quick look at the results
print('=== Using the Brown dataset ===')
print('Total number of words in the corpus vocabulary: {}\n'.format(len(features2.vocabulary_)))
print('10 random words from the vocabulary:\n\t {}\n'.format(list(features2.vocabulary_)[0:10]))
# Some more statistics:
print('Total number of documents in corpus: {}\n'.format(len(my_corpus)))
print('Statistics for each document:')
matrix = count_matrix2.toarray()  # Return a dense ndarray representation of the sparse matrix (same shape & data)
for i in list(range(0, len(my_corpus))):
    print('\tDoc {}: Words = {}, Unique words: {}'.format(i, len(my_corpus[i].split(' ')),
                                                          len(matrix[i, matrix[i, ] != 0])))
print('')
# Code explanation:
# - len(my_corpus[i].split(' ')) --> split the document into its words, then count the words
#       my_corpus[0] = the 1st document of the corpus
# - len(matrix[i, matrix[i, ] != 0] --> only select the elements that have a count different than zero, then count them
#       some elements have 0 --> this word is not present in the document
#       some elements have 1 --> this word is present only once in the document
#       some elements have C --> this word is present C times in the document

# ###############
# Part 3
# Visualise the document-term matrix nicely, using our custom function
# see 'print_dtm' in NLP_baselibrary
words_to_print = 5
start_index = 100  # index of the first word/feature to print
print_dtm(features2, count_matrix2, [start_index, start_index+words_to_print])
