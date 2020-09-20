# Intro to NLP with Python - a series in 9 steps
# Step 1: Tokenizer
#
# Author: Luca Naso - contact: www.lucanaso.it
# Contributors: empty for now
# URL: www.lucanaso.it/
# License: GNU CPL v3.0, see the LICENSE file.
# Natural Language: Italian for the blog post, English for the code
#

# ### Import section
# Import (3) tokenizers from nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

# Create a dataset to be used as input for the tokenizers.
# We use a simple citation from Dean Karnazes
text_run = 'Corro perché se non lo facessi sarei pigro e triste e spenderei il mio tempo sul divano. ' \
           'Corro per respirare l’aria fresca. Corro per esplorare. Corro per sfuggire l’ordinario. ' \
           'Corro... per assaporare il viaggio lungo la strada. La vita diventa un po’ più vivace, ' \
           'un po’ più intensa. A me questo piace. (Dean Karnazes)'
# print input data
print('Input data: \n\t{}'.format(text_run))

# ### Tokenizer 1
# Tokenize the text by sentence
sentence_tokenizer_output = sent_tokenize(text_run)
# print the tokens
print('\nOutput data (via Sentence Tokenizer):')
for token in sentence_tokenizer_output:
    print('\t{}'.format(token))

# ### Tokenizer 2
# Tokenize the text by word
word_tokenizer_output = word_tokenize(text_run)
# print the tokens
print('\nOutput data (via Word Tokenizer):')
for token in word_tokenizer_output:
    print('\t{}'.format(token))

# ### Tokenizer 3
# Tokenize the text by word with Regex
custom_tokenizer = RegexpTokenizer('\w+')
custom_tokenizer_output = custom_tokenizer.tokenize(text_run)
# print the tokens
print('\nOutput data (via Custom Tokenizer):')
for token in custom_tokenizer_output:
    print('\t{}'.format(token))

# ### Final Recap
print('\n\n--- Final Recap ---')
#
# 1. Show the input text
# and the number of tokens from each tokenizer
print('\nInput data: \n{}'.format(text_run))
print('- Tot sentences = {}'.format(len(sentence_tokenizer_output)))
print('- Tot words = {}'.format(len(word_tokenizer_output)))
print('- Tot words (via regex) = {}'.format(len(custom_tokenizer_output)))
#
# 2. For each sentence (as identified by tokenizer 1)
# print the result of the (2) tokenizers by word
print('\nEvaluate sentence by sentence:')
for i, sentence in zip(list(range(1, len(sentence_tokenizer_output))), sentence_tokenizer_output):
    print('Sentence {} = "{}"'.format(i, sentence))
    word_tokenizer = word_tokenize(sentence)
    print('\t Word Tokenizer, {} words: {}'.format(len(word_tokenizer), word_tokenizer))
    regex_tokenizer = custom_tokenizer.tokenize(sentence)
    print('\t Regex Tokenizer, {} words: {}'.format(len(regex_tokenizer), regex_tokenizer))

# End of Step 1
