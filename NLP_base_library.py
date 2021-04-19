# Author: Luca Naso - contact: www.lucanaso.it
# Creation date: 29 Jan 2021
# Contributors: empty for now
# URL: https://lucanaso.it/2021/02/03/splitting-nlp-di-base-in-python-4-di-9/
# License: GNU GPL v3.0, see the LICENSE file.
# Natural Language: blog post in Italian, code in English
# Topic: Intro to basic NLP in Python - a series in 9 steps
#        Library with functions, created in step 4
#


# Function to split text into chunks (first appeared in step 4 of the original series)
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
    # Usually the total number of words in the text is not a multiple of the chunk_size. In this case:
    # the last (current) chunk does not reach the target size,
    # to avoid losing the data we add the smaller chunk.
    if current_chunk_words:
        chunk = ' '.join(current_chunk_words)
        output_chunks.append(chunk)
    return output_chunks


# function to nicely print a document-term matrix (first appeared in step 5 of the original series)
def print_dtm(count_vectorizer_obj, dtm, print_indices):
    # print the matrix with words on rows and documents on cols
    # read the total number of documents
    tot_docs = len(dtm.toarray())
    # set the print format
    row_format = '{:^5}|' + '{:^15}|' + '{:^8}|'*tot_docs
    row_length = 1 + 5 + 15 + 9 * tot_docs+1
    # print the header
    print('\n'+'-' * row_length)
    doc_names = []
    for number in range(tot_docs):
        doc_names.append('Doc-{:02d}'.format(number+1))
    print(row_format.format('#', 'Word', *doc_names))
    print('-' * row_length)
    # print the rows
    start = print_indices[0]  # index of the first word/feature
    end = print_indices[1]  # index of the last word/feature
    for i, word, count in zip(range(start, end), count_vectorizer_obj.get_feature_names()[start:end],
                              dtm.T.toarray()):
        print(row_format.format(i+1, word, *count))
    print('-' * row_length)
