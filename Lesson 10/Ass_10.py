import tkinter as tk
import palindrome_checker 

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label_1 = tk.Label(self, text='Welcome to the palindrome finder! please enter a word or sentence: ', fg= '#6D2932', bg='#E8D8C4')
        self.label_1.pack()
        self.entry_0 = tk.Entry(self, fg= '#6D2932', bg='#FDF0D1')
        self.entry_0.pack()
        self.label_2 = tk.Label(self, fg='#6D2932')
        self.label_2.pack()
        self.spacer1 = tk.Label(self, text="", font=('Times New Roman', 20))
        self.spacer1.pack()                                       
        self.btn = tk.Button(self, text ='Submit', command=self.submit)
        self.btn.pack()
        
    def submit(self):
        palindrome_checker.palindrome_checker(self)

root = Root()
root.title("Palindrome checker")
root['bg'] = '#E8D8C4'

root.mainloop()
