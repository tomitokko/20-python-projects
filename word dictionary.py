from PyDictionary import PyDictionary

def main():
    dictionary = PyDictionary()

    input_word = input("Input word you wanna translate: ") #made user input for words

    print(dictionary.meaning(input_word[0])) #just show about first sentence

#code for replay again
print("Welcome To Our Word Translate!!")
while True:
    input_again = input('Wanna Translate ? (y/n) ')
    if input_again == 'Y' or input_again == 'y':
        main()
    else:
       break
