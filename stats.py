#! /usr/bin/env python3

# function returns the number of words in a text
def get_num_words(text):
    return len(text.split())

# function returns the number of characters in a text
def get_num_chars(text):
    format_text = text.lower()
    char_count = {}
    for char in format_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# function to sort a list of dictionaries
# states when you are comparing two dictionaries, use the 'num' value to determine order
def sort_on(item):
    return item['num']

# function to sort a dictionary
# convert the dictionary to a list of smaller dictionaries
# sorted by the number of occurrences of each character
def sorted_dict(dict):
    char_num_list = []
    for key, value in dict.items():
        if key.isalpha():
            char_num_list.append({'char': key, 'num': value})
    char_num_list.sort(reverse=True, key=sort_on)
    return char_num_list

