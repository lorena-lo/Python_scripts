""" This module replaces identified words form a text (paragraph, phrase etc.) with other words given. It
receives 2 information: the text to be modified and a nested list of values, as fallows: [[start,stop, new_word],
[start,stop, new_word],...
This module has the following tasks:
-Creates a mapping between the identified at the given location (between start-stop) word in the text (named here: old
words), with the new word received;
 -Modifies the text, removing the old words and adding the new words instead."""
from ast import literal_eval


def create_dict(original_phrase, to_modify_list):
    dict_words = {}
    for i in to_modify_list:
        start, stop, word = i
        word = word.strip()
        dict_words[word] = original_phrase[start:stop].strip()
    return dict_words


def modify_phrase(original_phrase, dict_words):
    for key in dict_words.keys():
        original_phrase = original_phrase.replace(dict_words[key], key)
    return original_phrase


if __name__ == "__main__":
    original_phrase = 'Lorem Ipsum este pur şi simplu o macheta pentru text a industriei tipografice.'
    to_modify_list = [[17, 30, "cu siguranta"], [33, 40, "emblema"], [66, 77, "informatice"]]
    words = create_dict(original_phrase, to_modify_list)
    print(modify_phrase(original_phrase, words))
