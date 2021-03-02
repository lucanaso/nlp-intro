# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 25 Jan 2021
# Contributors: empty for now
# URL: https://lucanaso.it/2021/02/03/splitting-nlp-di-base-in-python-4-di-9/
# License: GNU GPL v3.0, see the LICENSE file.
# Natural Language: blog post in Italian, code in English
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Step 4: Text-splitting
#

def text_splitting(input_text, chunk_size):
    output_chunks = []  # this is where we will be storing all of the chunks
    current_chunk_size = 0  # a counter to keep track of the number of words in the chunk
    current_chunk_words = []  # a list with the words to include in the chunk
    all_words = input_text.split(' ')  # split the whole input_text by white spaces
    for word in all_words:
        current_chunk_words.append(word)  # add the word to the chunk words
        current_chunk_size += 1  # update the chunk size
        if current_chunk_size == chunk_size:  # check if the chunk contains the desired number of words
            chunk = ' '.join(current_chunk_words)  # bring the words back together to create a readable chunk
            output_chunks.append(chunk)  # add the chunk to the final list
            # reset 'current' variables:
            current_chunk_words = []
            current_chunk_size = 0
    # Usually the total number of words in the text is not a multiple of the chunk_size.
    #     In this case: the last (current) chunk does not reach the target size,
    #     to avoid losing the data we add the smaller chunk.
    if current_chunk_words:
        chunk = ' '.join(current_chunk_words)
        output_chunks.append(chunk)
    return output_chunks


# read data from file
filename = 'text_run_eng.txt'
with open(filename, 'r') as reader:
    input_raw_text = reader.read()
print('\nInput raw text is: \n{}\n'.format(input_raw_text))

# set the parameters for splitting the text
words_in_chunk = 10

# split the input text, call our new function:
output = text_splitting(input_raw_text, words_in_chunk)

# print some general statistics
print('# General Statistics')
tot_chunk = len(output)
print('- The original text contains {} words'.format(len(input_raw_text.split(' '))))
print('- The desired chunk size is {} words'.format(words_in_chunk))
print('==>\n- The splitting function created {} chunks. Here they are:'.format(tot_chunk))
for i, chunk in zip(list(range(0, tot_chunk)), output):
    print('\tChunk n. {} ({} words) = {}'.format(i+1, len(chunk.split(' ')), chunk))
