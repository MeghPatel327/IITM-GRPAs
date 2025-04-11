# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <nofor>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# The values of the below variables will be changed by the evaluator
int_iterable = range(1,10,3)
string_iterable = ["Apple","Orange", "Banana"]
some_value = 4
some_collection = [1,2,3] # list | set | tuple 

some_iterable = (1,2,3)
another_iterable = {"apple", "banana", "cherry"} # can be any iterable
yet_another_iterable = range(1,10)

# <nofor>
# <eoi>

empty_list = [] 
empty_set = set([]) # be carefull here you might end up creating something called as an empty dict 
empty_tuple = () 

singleton_list = [1,] # list: A list with only one element
singleton_set = {1,} # set: A set with only one element
singleton_tuple = (1,) # tuple: A tuple with only one element

a_falsy_list = [] # list: a list but when passed to bool function should return False.
a_falsy_set = set() # set: a list but when passed to bool function should return False.
a_truthy_tuple = (1,) # tuple: a tuple but when passed to bool function should return True

int_iterable_min = min(int_iterable) # int: find the minimum of int_iterable. Hint: use min function
int_iterable_max = max(int_iterable) # int: find the maximum of int_iterable. Hint: use max function
int_iterable_sum = sum(int_iterable) # int: you know what to do
int_iterable_len = len(int_iterable) # int: really... you need hint?
int_iterable_sorted = sorted(int_iterable) # list: the int_iterable sorted in ascending order
int_iterable_sorted_desc = sorted(int_iterable,reverse=True) # list: the int_iterable sorted in desc order

if 'set' not in str(type(int_iterable)) : # some iterables are not reversible why?
    int_iterable_reversed = int_iterable[::-1] # list: the int_iterable reversed use the reversed function
else: # in that case sort it in ascending order and reverse it
    int_iterable_reversed = sorted(int_iterable)[::-1] #list

if 'set' not in str(type(some_collection )) : # some collections are not indexable why?
    third_last_element = some_collection [-3] # the third last element of `some_collection`
else: # in that case set third_last_element to None
    third_last_element = None

if 'set' not in str(type(some_collection )) : # some collections are not slicable
    odd_index_elements = some_collection[1::2] # type(some_collection): the elements at odd indices of `some_collection` 
else: # in that case set odd_index_elements to None
    odd_index_elements = None

is_some_value_in_some_collection = True if some_value in some_collection else False # bool: True if `some_value` is present in `some_collection`

if 'set' not in str(type(some_collection )) : # some collections are not ordered
    is_some_value_in_even_indices = True if some_value in some_collection[0::2] else False # bool: True if `some_value` is present in even indices of `some_collection`
else: # in that case set is_some_value_in_even_indices to None
    is_some_value_in_even_indices = None

all_iterables = list(some_iterable) + list(another_iterable) + list(yet_another_iterable) # list: concatenate `some_iterable`, `another_iterable` and `yet_another_iterable` into a list.

if 'set' not in str(type(string_iterable )) : # some iterables are not ordered
    all_concat = ''
    i = 0 
    while i < len(string_iterable):
        all_concat += string_iterable[i] + '-'
        i+=1
    all_concat = all_concat[:len(all_concat)-1]

else: # in that case sort them and concatenate
    all_concat = ''
    string_iterable = list(sorted(string_iterable))
    i = 0 
    while i < len(string_iterable):
        all_concat += string_iterable[i] + '-'
        i+=1 
    all_concat = all_concat[:len(all_concat)-1]