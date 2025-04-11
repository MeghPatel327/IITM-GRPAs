class StringManipulation:
    def __init__(self, l:list):
        self.l = l
    
    def total_words(self):
        return len(self.l)
    
    def count(self, some_word):
        return self.l.count(some_word)
    
    def words_of_length(self, length):
        return [word for word in self.l if len(word) == length]
    
    def words_start_with(self, char):
        return [word for word in self.l if word.startswith(char)]
    
    def longest_word(self):
        return max(self.l, key=len)
    
    def palindromes(self):
        return [word for word in self.l if word == word[::-1]]