sentence = input("Enter sentence: ")
sent  = sentence.split()
file = open("words_.txt",'r', encoding='utf8')
word_list = file.readlines()
sent_out =[]
for word in sent:
    for wrd in word_list:
        word_eng = (((wrd.strip()).split('-'))[0]).strip()
        words_sin = (((((wrd.strip()).split('-'))[1]).split("|"))[0]).strip()
        #print(word_eng)
        if ((word.strip()) == word_eng):
            sent_out.append(words_sin)
            break
file.close()

for i in sent_out:
    print(i, end=" ")