# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 22 Sep 2020
# Contributors: empty for now
# URL: https://lucanaso.it/2020/10/06/stemming-nlp-di-base-in-python-2-di-9/
# License: GNU CPL v3.0, see the LICENSE file.
# Natural Language: Italian for the blog post, English for the code
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Step 2: Stemming
#

# ### Import section
# Import 3 stemmers and 1 tokenizer from nltk
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
from nltk.tokenize import RegexpTokenizer

# ###    Quick example    ###
# create an instance of the Snowball stemmer, optimised for the Italian language
stemmer_snowball = SnowballStemmer('italian')
# create two example word-lists
eg1 = ['correre', 'corro', 'corriamo', 'correremo']
eg2 = ['bambino', 'bambini', 'bambina', 'bambine']
# merge the lists together
eg_list = []
eg_list.extend(eg1)
eg_list.extend(eg2)
# do a for loop on both lists, apply the stemmer to each word and print the result
print('\n= Quick stemming example =')
print('Input words: {}\nCorresponding stemmed words:'.format(eg_list))
for word in eg_list:
    print('\t- {}'.format(stemmer_snowball.stem(word)))

# ###    Prepare input data    ###
# read data from file
filename = 'text_run_eng.txt'
with open(filename, 'r') as reader:
    input_raw_text = reader.read()
    print('\nInput raw text is: \n{}'.format(input_raw_text))
# split data into words
custom_tokenizer = RegexpTokenizer('\w+')
word_list = custom_tokenizer.tokenize(input_raw_text)

# ###    Stemming    ###
# Create Stemmer instances
stemmer_porter = PorterStemmer()
stemmer_lancaster = LancasterStemmer()
stemmer_snowball = SnowballStemmer('english')
# stem each word and print results
print('\nStemming {} words with Porter, Snowball and Lancaster respectively.'.format(len(word_list)))
for word in word_list:
    print('{0}: {1}, {2}, {3}'.format(
        word,
        stemmer_porter.stem(word),
        stemmer_snowball.stem(word),
        stemmer_lancaster.stem(word))
    )
# Note that:
#   - Lancaster and Snowball apply lowercase to *any* input word
#   - Porter doesn't

# ###    Visualisation    ###
# Improve the visualisation for easier stemmer comparison
# Use a Table style, with 4 columns and as many rows as words
#   for each row we print the original word + the 3 stemmed words.
print('\nStemming {} words\n'.format(len(word_list)))
header = ['Original Word', 'Porter', 'SnowBall', 'Lancaster']
row_format = '{:<15}:' + '{:^15} -' * 2 + '{:^15}|'
# 1st column: align left, use 15 characters plus a colon ":"
# 2nd + 3rd columns: align center, use 15 characters plus " -"
# 4th column: align center, use 15 characters plus a pipe "|"
print(row_format.format(*header))  # print all elements of the header list
                                   # *<list> performs an unpacking of the list
print('-'*66)  # print a kind of separation line, between header and rows
# print each word
for word in word_list:
    stemmed_words = [stemmer_porter.stem(word),
                     stemmer_snowball.stem(word),
                     stemmer_lancaster.stem(word)]
    print(row_format.format(word, *stemmed_words))
# print again the header, at the bottom of the table
print('-'*66)
print(row_format.format(*header))

# ###    Improvements    ###
# remove duplicates: from 60 to 38 words (ita: from 56 to 43)
word_list_unique = list(set(word_list))
# remove words with less than 4 characters: from 38 to 24 words (ita: from 43 to ?)
word_list_final = [x for x in word_list_unique if len(x) > 3]
# print final results
print('\nStemming {} unique words, longer than 3 characters\n'.format(len(word_list_final)))
# header = ['Original Word', 'Porter', 'SnowBall', 'Lancaster']
# row_format = '{:<15}:' + '{:^15} -' * 2 + '{:^15}|'
# same header and row format as earlier
print(row_format.format(*header))
print('-'*66)  # print a kind of separation line, between header and rows
for word in word_list_final:
    stemmed_words = [stemmer_porter.stem(word),
                     stemmer_snowball.stem(word),
                     stemmer_lancaster.stem(word)]
    print(row_format.format(word, *stemmed_words))
# print again the header, at the bottom of the table
print('-'*66)
print(row_format.format(*header))

# End of Step 2
