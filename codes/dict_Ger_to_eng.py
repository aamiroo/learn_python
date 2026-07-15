"""
This app is a German-English and English-German dictionary.
With json file
User activity
"""
import json

words = {}
#import json data for dictinary
with open("dictionary-de.json","r") as fd:
    dictionary = {}
    for line in fd:
        data = json.loads(line)

        german = data.get("") #giv valiu from key
        meaning = data.get("d", []) #add to meaning

        if german and meaning: #creat dictionary
            dictionary[german.lower()] = meaning


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
words.update(dictionary) #add json to my dict

revers_words = {}
for german , english_list in words.items():
    for english in english_list:
        revers_words[english.lower()] = german


def search (words , word):
    if word in words:
        return(words[word])
    elif word in revers_words:
        return revers_words [word]
    else:
        return "not information"
while True:
    try: 
        print()
        word = input("please enter your word: \n-press enter Q for exit\n").lower()
        if word == "q":
            break
        print(search (words , word))
    except Exception as e:
        print(e)

