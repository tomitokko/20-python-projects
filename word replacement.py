def replace_word():
    str = input("Words i wanna type: ") #made word with input from user
    word_to_replace = input("Enter The Word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))
    back = input("Still wanna play this game : (y/n) ? ")
    if back == 'y' or back == 'Y': #made replay game if input = y or Y
        return replace_word()
        
replace_word()
