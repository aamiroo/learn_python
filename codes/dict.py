words = {}

words['hallo'] = ['hello']
words['buch'] = ['book']
words['uhr'] = ['clock']
words['welt'] = ['world']
words['müde'] = ['tired']
words['lrieg'] = ['war']
words['Geschichte'] = ['history']
words['fehler'] = ['error']
words['kammentar'] = ['coment']
words['König'] = ['king']


def search (words , word):
    if word in words:
        return(words[word])
    else:
        return "not information"

word = input("please enter your word: ")
print(search (words , word))

