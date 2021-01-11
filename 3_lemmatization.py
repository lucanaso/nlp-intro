# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 03 Nov 2020
# Contributors: empty for now
# URL: https://lucanaso.it/2021/01/11/lematization-nlp-di-base-in-python-3-di-9/
# License: GNU GPL v3.0, see the LICENSE file.
# Natural Language: blog post in Italian, code in English
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Step 3: Lemmatization
#

# ### Import section
# nltk.download('averaged_perceptron_tagger')  # only once
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
from nltk.corpus import wordnet

# There are several packages that can be used to implement Lemmatizaion in Python.
#   We will use the Wordnet Lemmatizer
#   Wordnet is an large, freely and publicly available lexical database for the English language
#   NLTK offers an interface to it
#
# Quick Lemmatizer and Stemming comparison
print('\n=== Get a lemma quickly ===\n')
first_lemmatizer = WordNetLemmatizer()
usual_stemmer = SnowballStemmer('english')
input_wordlist = ['wolves', 'wolf']
for word in input_wordlist:
    lemma = first_lemmatizer.lemmatize(word)
    stem = usual_stemmer.stem(word)
    print('Input word: \t{}'.format(word))
    print('\tOutput Lemma: \t{}'.format(lemma))
    print('\tOutput Stem: \t{}\n'.format(stem))

# We want to apply the lemmatizer to a longer text (rather than a few words)
#   just as stemming the lemmatizer operates on words,
#   so we proceed as we did with stemming,
#       i.e. we create a list of words and then apply the lemmatizer to each word
# We use a function to do this


def split_to_words(input_filename):
    # read data from text file
    with open(input_filename, 'r') as reader:
        input_raw_text = reader.read()
        print('\nInput raw text is: \n{}'.format(input_raw_text))
    # split data into words
    custom_tokenizer = RegexpTokenizer('\w+')
    word_list = custom_tokenizer.tokenize(input_raw_text)
    return word_list


# Test the newly created function
test_filename = 'text_run_eng.txt'
test_word_list = split_to_words(test_filename)

# ###    Prepare input data    ###
# Get the data with our custom function
filename = 'text_lotr_sam_turningback.txt'
word_list = split_to_words(filename)
# remove duplicates
word_list_unique = list(set(word_list))
# remove words with less than 4 characters
word_list_final = [x for x in word_list_unique if len(x) > 3]

# Create the instance of the Lemmatizer
lemmatizer = WordNetLemmatizer()
# apply the lemmatizer to the word list and store result into a new list
lemma_list = []
for word in word_list_final:
    lemma_list.append(lemmatizer.lemmatize(word))

# in order to work best, Lemmatization needs to know the kind of word it is working on,
#   e.g. it should know if the word is a noun, a verb or something else.
#   this can be done simply by passing the POS (Part Of Speech) tag to the lemmatizer.
# ###   Testing the PoS   ###
print('\nGet a lemma using PoS')
test_word = 'known'
print('Testing the word "{}"'.format(test_word))
print('\t Lemma when using "noun" = {}'.format(lemmatizer.lemmatize(test_word, pos='n')))  # if no 'pos' is passed, 'pos=n' is the default
print('\t Lemma when using "verb" = {}'.format(lemmatizer.lemmatize(test_word, pos='v')))
# where pos='n' means Part Of Speech = noun
# and pos='n' means Part Of Speech = verb
#   Wordnet (used by WordNetLemmatizer) accepts 5 POS tags:
#   As in the source code of nltk.corpus.reader.wordnet
#   http://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html
#   { Part-of-speech constants
#       ADJ, ADJ_SAT, ADV, NOUN, VERB = "a", "s", "r", "n", "v"
#   }
#


# Compare results of Stemming and Lemmatizing (with noun and with verb)
def compare_lemmatize_vn_stemmer(word_list):
    # for each word of the input list
    #   get the stemmed word
    #   get the lemmas with pos = noun and pos = verb
    #   print the original word, the stem and the two lemmas
    stemmer_snowball = SnowballStemmer('english')
    header = ['Original', 'Stem', 'Lemma noun', 'Lemma verb']
    row_format = '{:>10}:' + '  {:^12} -' * 2 + '{:^12}|'
    print('-' * 56)
    print(row_format.format(*header))
    print('-' * 56)
    for word in word_list:
        stemmed = stemmer_snowball.stem(word)
        lemma_n = lemmatizer.lemmatize(word, pos='n')
        lemma_v = lemmatizer.lemmatize(word, pos='v')
        print(row_format.format(word, stemmed, lemma_n, lemma_v))
    print('-' * 56 + '\n')
    return


print('\nTesting effect of POS and comparison with Stemming')
print('Test with verb "to go"')
input_wordlist = ['gone', 'goes', 'went', 'go']
compare_lemmatize_vn_stemmer(input_wordlist)
print('Test with verb "to dream"')
input_wordlist = ['dreamt', 'dreams', 'dreaming', 'dream']
compare_lemmatize_vn_stemmer(input_wordlist)
print('Test with noun "wolf"')
input_wordlist = ['wolves', 'wolf']
compare_lemmatize_vn_stemmer(input_wordlist)
# we see that, when using the appropriate POS, the same Lemma is returned for all variations


# AUTO-TAGGING
# We do not want to pass the pos_tag by hand for each word in our list,
#   we are lucky, because an off-the-shelf tagger is available for English
#   so we use nltk.pos_tag([word_1, word_2, ...]) to get the pos_tag automatically of each word
# TEST for post_tag
print('Auto tag for the test word "{}" = {}'.format(test_word, pos_tag([test_word])))
auto_tag = pos_tag([test_word])[0][1]
print(auto_tag)

# pos_tag returns a list of tuple with 2 elements each: (word, pos_tag)
#   e.g. [('spend', 'NN')]
#   where 'NN' is the term used to indicate the Part Of Speech by the pos_tag function.
# pos_tag returns tags from a list of 35 values:
#     CC coordinating conjunction
#     CD cardinal digit
#     DT determiner
#     EX existential there (like: “there is” … think of it like “there exists”)
#     FW foreign word
#     IN preposition/subordinating conjunction
#     JJ adjective ‘big’
#     JJR adjective, comparative ‘bigger’
#     JJS adjective, superlative ‘biggest’
#     LS list marker 1)
#     MD modal could, will
#     NN noun, singular ‘desk’
#     NNS noun plural ‘desks’
#     NNP proper noun, singular ‘Harrison’
#     NNPS proper noun, plural ‘Americans’
#     PDT predeterminer ‘all the kids’
#     POS possessive ending parent’s
#     PRP personal pronoun I, he, she
#     PRP$ possessive pronoun my, his, hers
#     RB adverb very, silently,
#     RBR adverb, comparative better
#     RBS adverb, superlative best
#     RP particle give up
#     TO, to go ‘to’ the store.
#     UH interjection, errrrrrrrm
#     VB verb, base form take
#     VBD verb, past tense, took
#     VBG verb, gerund/present participle taking
#     VBN verb, past participle is taken
#     VBP verb, sing. present, known-3d take
#     VBZ verb, 3rd person sing. present takes
#     WDT wh-determiner which
#     WP wh-pronoun who, what
#     WP$ possessive wh-pronoun whose
#     WRB wh-adverb where, when
# WordNet Lemmatizer instead only accepts 5 values
#   (ADJ, ADJ_SAT, ADV, NOUN, VERB,
#    "a",     "s", "r",  "n",  "v")
# So we need to map the post_tag output into the one of the values accepted by the lemmatizer
# We do this with a new function


def map_postag_into_wordnet(postag):
    # input: value from pos_tag
    # output: value for WordNet lemmatizer
    # mapping logic:
    #   pos_tags that begin with J are adjectives
    #                       with V are verbs
    #                       with N are nouns
    #                       with R are adverbs
    #
    # Create a dictionary with the mapping:
    tag_map = {"j": wordnet.ADJ,
               "n": wordnet.NOUN,
               "v": wordnet.VERB,
               "r": wordnet.ADV}
    # Create a default option, to be used when the mapping fails:
    default_pos = wordnet.NOUN
    # Now return the value for the appropriate key (key = 1st letter of the postag)
    #   if the key is not found, return the chosen default
    wordnet_tag = tag_map.get(postag[0].lower(), default_pos)
    return wordnet_tag


# TEST for map_postag_into_wordnet function:
test_pos_tag = ['JJ', 'NNS', 'VBN', 'RBR', 'missing_tag']
print('\nTest for the mapping function:')
for input_tag in test_pos_tag:
    mapped_tag = map_postag_into_wordnet(input_tag)
    print('\tInput tag \'{}\' is mapped into \'{}\''.format(input_tag, mapped_tag))

# Let's put the two parts together and then use them in the Lemmatizer:
#   1. auto-tag with pos_tag
#   2. mapping with our custom function (map_postag_into_wordnet)
#   3. use Lemmatizer with the new tag
auto_tag = pos_tag([test_word])[0][1]  # step 1
wrdnt_tag = map_postag_into_wordnet(auto_tag)  # step 2
lemma_2 = lemmatizer.lemmatize(test_word, pos=wrdnt_tag)  # step 3
print('\nGet the lemma using auto-tagging and custom mapping function.')
print('\tInput word = \'{}\' ---> Lemma = \'{}\' \t(tag = {})'.format(test_word, lemma_2, wrdnt_tag))


# Get the lemmas for all of the words:
print('\nGet the lemmas with PoS for all of the words...')
tagged_word_list = pos_tag(word_list_final)  # list of tuples with (word, postag)
lemma_list = []
for word, tag in tagged_word_list:  # split each tuple within the loop
    wrdnt_tag = map_postag_into_wordnet(tag)
    lemma = lemmatizer.lemmatize(word, pos=wrdnt_tag)
    lemma_list.append(lemma)


# Function for my Comparison Table
def print_cmp_table1(header, row_format, row_length, col1, col2, col3, col4):
    print(row_format.format(*header))
    print('-' * row_length)
    for c1, c2, c3, c4 in zip(col1, col2, col3, col4):
        print(row_format.format(c1, c2, c3, c4))
    print('-' * row_length)
    print(row_format.format(*header))


# Print a comparison table for Stemmer, Lemmatizer without PoS and Lemmatizer with PoS
# for the whole input text
print('\n\nComparison among Stemmer, Lemmatizer without PoS (i.e. use noun for all the words) '
      'and Lemmatizer with PoS on the whole text.\n')
# Get the list of words for the Stemmer and for the Lemmatizer without PoS
stemmer_snowball = SnowballStemmer('english')
stem_list = []
lemma_wo_POS = []
for word in word_list_final:
    stem_list.append(stemmer_snowball.stem(word))
    lemma_wo_POS.append(lemmatizer.lemmatize(word))
# Set the parameters for the comparison table
header = ['Original Word', 'SnowBall', 'Lemmatizer wo PoS', 'Lemmatizer w PoS']
row_format = '{:<15}:' + '{:^12} -' + '{:^20} -' + '{:^21}|'
raw_length = 74
# call the function
print_cmp_table1(header, row_format, raw_length, word_list_final, stem_list, lemma_wo_POS, lemma_list)

# End of Step 3
