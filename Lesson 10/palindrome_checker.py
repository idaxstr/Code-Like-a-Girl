
def palindrome_checker(self):
        self.word = self.entry_0.get()
        self.word_lower = self.word.lower().replace(" ", "")
        self.word_list = list(self.word_lower)
        self.word_list.reverse()
        self.new_word = ''.join(self.word_list)
        if (self.word_lower == self.new_word):
            self.label_2['text'] = (f'{self.word} is a palindrome')
        else:
            self.label_2['text'] = (f'{self.word} is not a palindrome')
