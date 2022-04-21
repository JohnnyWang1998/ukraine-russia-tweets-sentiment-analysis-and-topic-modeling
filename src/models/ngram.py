import numpy as np


def make_ngrams(tokens: list, n: int) -> list:
    """Creates n-grams for the given token sequence.
    Args:
    tokens (list): a list of tokens as strings
    n (int): the length of n-grams to create

    Returns:
    list: list of tuples of strings, each tuple being one of the individual n-grams
    """
    n_grams = []

    for token in tokens:
        word_list = token.split(" ")  # split with whitespace

        # initialize index
        starting_index = 0
        end_index = starting_index + n - 1

        # use sliding window to append tuples of length n to n_grams
        while end_index < len(word_list):
            n_grams.append(tuple(word_list[starting_index: starting_index + n]))
            starting_index += 1
            end_index += 1

    return n_grams


def train_ngram(content, n_gram):
    # Get the count of each word
    UNK = "<UNK>"
    word_count = {}
    for line in content:
        for word in line:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count[word] = 1

    # Replace the words with <UNK> if count is < threshold(=1)
    UNK_count_dict = dict(
        filter(lambda elem: elem[1] == 1, word_count.items()))  # get dictionary of words whose count == 1
    word_count[UNK] = len(UNK_count_dict)  # add UNK to word_count
    for temp_key in UNK_count_dict.keys():  # pop count == 1 words from word_count
        word_count.pop(temp_key, None)

    # make use of make_n_grams function

    n_gram_counts = {}
    for line in content:
        for ngram_tuple in make_ngrams(line, n_gram):
            if ngram_tuple in n_gram_counts.keys():
                n_gram_counts[ngram_tuple] += 1
            else:
                n_gram_counts[ngram_tuple] = 1

    # Get the training data vocabulary
    vocab = list(word_count.keys())

    # For n>1 grams compute n-1 gram counts to compute probability
    n_minus_1_gram_counts = {}
    if n_gram > 1:
        for line in content:
            for n_minus_1_gram_tuple in make_ngrams(line, n_gram - 1):
                if n_minus_1_gram_tuple in n_minus_1_gram_counts.keys():
                    n_minus_1_gram_counts[n_minus_1_gram_tuple] += 1
                else:
                    n_minus_1_gram_counts[n_minus_1_gram_tuple] = 1

    return n_gram_counts, vocab, n_minus_1_gram_counts, word_count


def generate_sentence(n_gram_counts, vocab, n_minus_1_gram_counts, word_count, n_gram=5, max_length=20):
    """Generates a single sentence from a trained language model using the Shannon technique.

    Returns:
      str: the generated sentence
    """
    # Start with <s> and randomly generate words until we encounter sentence end
    # Append sentence begin markers for n>2
    # Keep track of previous word for stop condition
    SENT_BEGIN = "<s>"
    SENT_END = "</s>"

    n = n_gram
    sentence = [SENT_BEGIN]
    if n > 2:
        for i in range(0, n - 2):
            sentence.insert(0, SENT_BEGIN)

    if n > 1:
        while sentence[-1:][0] != SENT_END and len(sentence) <= max_length:
            # Construct the (n-1) gram so far
            n_minus_one = tuple(sentence[-(n - 1):])

            # Get the counts of all available choices based on n-1 gram
            choices_and_counts = {}

            for key in n_gram_counts:
                if n_minus_one == key[:n - 1]:
                    choice = list(key[-1:])[0]
                    count = n_gram_counts[key]
                    choices_and_counts[choice] = count
            # Convert the counts into probability for random.choice() function
            temp_sum = sum(list(choices_and_counts.values()))
            for choice in choices_and_counts:
                choices_and_counts[choice] = (choices_and_counts[choice]) / temp_sum

            while True:
                word_generated = np.random.choice(list(choices_and_counts.keys()), 1,
                                                  list(choices_and_counts.values())).astype(str)
                if word_generated != SENT_BEGIN:
                    break
            sentence.append(word_generated[0])

        # If <s> is generated, ignore and generate another word
    else:
        # In case of unigram model, n-1 gram is just the previous word and possible choice is whole vocabulary
        while sentence[-1:][0] != SENT_END:
            # Convert the counts into probability for random.choice() function
            temp_sum = sum(list(word_count.values()))
            for choice in word_count:
                word_count[choice] = word_count[choice] / temp_sum

            while True:
                word_generated = np.random.choice(list(word_count.keys()), 1, list(word_count.values())).astype(str)
                if word_generated != SENT_BEGIN:
                    break

            sentence.append(word_generated[0])
            # If <s> is generated, ignore and generate another word

    # Append sentence end markers for n>2
    if n > 2:
        for i in range(0, n - 2):
            sentence.append(SENT_END)
    return ' '.join(word for word in sentence)
