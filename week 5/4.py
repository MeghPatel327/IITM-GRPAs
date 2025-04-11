# mapping
def is_greater_than_5(numbers: list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    return list(map(lambda num: num > 5, numbers))

# filtering
def filter_less_than_5(numbers: list) -> list:
    '''Given a list of numbers, return a list of numbers that are less than 5'''
    return list(filter(lambda num: num < 5, numbers))

# aggregation with filtering
def sum_of_two_digit_numbers(numbers: list) -> int:
    '''Given a list of numbers, find the sum of all two-digit numbers.'''
    return sum(filter(lambda num: 10 <= num <= 99, numbers))

# aggregation with mapping
def is_all_has_a(words: list) -> bool:
    '''Given a list of words, check if all words have the letter "a" (case insensitive) in them.'''
    return all(map(lambda word: 'a' in word.lower(), words))

# enumerate
def print_with_numbering(items):
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple", "orange", "banana"]
    1. apple
    2. orange
    3. banana
    '''
    list(map(lambda i_item: print(f"{i_item[0] + 1}. {i_item[1]}"), map(lambda i: (i, items[i]), range(len(items)))))

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple lines separated by a hyphen with space around it.
    '''
    list(map(lambda pair: print(f"{pair[0]} - {pair[1]}"), zip(countries, capitals)))

# key-value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''
    return dict(zip(keys, values))

# enumerate with filtering and mapping
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of big words (length greater than 5).'''
    return list(map(lambda pair: pair[0], filter(lambda pair: len(pair[1]) > 5, zip(range(len(words)), words))))

# zip with mapping and aggregation
def decode_rle(chars: str, repeats: list) -> str:
    '''
    Create a string with the i-th char from chars repeated i-th value of repeats number of times. 

    Note: RLE refers to Run-length encoding.
    '''
    return ''.join(map(lambda pair: pair[0] * pair[1], zip(chars, repeats)))
