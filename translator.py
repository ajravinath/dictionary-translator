from tkinter import *


def trnaslate(sentence):
    # sentence = input("Enter sentence: ")
    translated = ''
    sent = sentence.split()
    file = open("words_.txt", 'r', encoding='utf8')
    word_list = file.readlines()
    sent_out = []
    for word in sent:
        for wrd in word_list:
            word_eng = (((wrd.strip()).split('-'))[0]).strip()
            words_sin = (((((wrd.strip()).split('-'))[1]).split("|"))[0]).strip()
            # print(word_eng)
            if ((word.strip()) == word_eng):
                sent_out.append(words_sin)
                break
    file.close()

    for i in sent_out:
        translated += (str(i)+" ")
    # print(i, end=" ")

    return translated

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text ="Enter the sentence")
        self.instruction.grid(row = 0,column=0,columnspan =2,sticky = W)

        self.sentence = Entry(self,width = 99)
        self.sentence.grid(row=1,column=0,sticky = W)

        self.submit_button = Button(self, text = 'Translate', command = self.reveal)
        self.submit_button.grid(row=3,column=0,sticky=W)

        self.text = Text(self, width = 74,height = 5,wrap=WORD)
        self.text.grid(row=5,column=0,columnspan=2,sticky=W)

    def reveal(self):
        content = self.sentence.get()
        self.text.delete('1.0', END)
        message = trnaslate(content)

        self.text.insert(0.0,message)

root = Tk()
root.title('Translator')
root.geometry('600x160')
app = Application(root)
root.mainloop()

