"""Given a word list, find the word with the most anagrams in the list."""


def find_most_anagrams_from_wordlist(word_list):
    """Given a list of words, return the word with the most anagrams.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """
    all_words = [w.strip() for w in open('words.txt')]
    # all_words = ['act', 'cat', ...]

    # create empty dict to store values and indeces of unique anagrams e.g. {'act': (2,0)}
    word_list_dict = {} 
    for word in word_list:
        sorted_word = ''.join(sorted(word)) # calling sorted on a string converts the string to a list, so join the list to convert word back to string
        first_word_index = word_list.index(word) # storing index of word to add to value tuple
        if sorted_word not in word_list_dict:
            word_list_dict[sorted_word] = (1, first_word_index) # value = (anagram count, index of first instance of anagram)
        else:
            original_index = word_list_dict[sorted_word][1] # accessing index in value tuple
            new_count = word_list_dict[sorted_word][0] + 1
            word_list_dict[sorted_word] = (new_count, original_index)

    # find keys with highest anagram count, 
    # check the indeces of the highest anagram counts and get lowest index, 
    # return word from word_list with the index of the key with the highest anagram count and lowest index
    highest_key = None
    for key in word_list_dict: 
        current_value = word_list_dict[key][0]
        if highest_key == None:
            highest_key = key
            highest_value = word_list_dict[highest_key][0]
        else:
            if current_value > highest_value:
                highest_key = key
                highest_value = word_list_dict[highest_key][0]
            elif current_value == highest_value:
                if word_list_dict[key][1] < word_list_dict[highest_key][1]:
                    highest_key = key
    return word_list[word_list_dict[highest_key][1]]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
