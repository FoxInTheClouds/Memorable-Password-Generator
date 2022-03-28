import secrets
import string


def random_based_generator(
        length, 
        include_uppercase, 
        include_numbers, 
        include_symbols):

    password = ""

    characters = string.ascii_lowercase

    if include_uppercase == 1:
        characters = characters + string.ascii_uppercase

    if include_numbers == 1:
        characters = characters + string.digits

    if include_symbols == 1:
        characters = characters + string.punctuation

    good_password = False
    while good_password == False:

        for i in range(0, length):
            password = password + secrets.choice(characters)

        if include_uppercase == 1:
            
            for i in password:
                if i.isupper() == True:
                    good_password = True

        if include_numbers == 1:
            
            for i in password:
                if i.isdigit() == True:
                    good_password = True 

        if include_symbols == 1:
            
            for i in password:
                if i in string.punctuation:
                    good_password = True

    return password


def word_based_generator(
        word_number, 
        include_uppercase, 
        include_numbers, 
        include_symbols, 
        uppercase_position, 
        numbers_position, 
        symbols_position):   
    
    word_list_file = open(r"final_list.txt", "r")  # Opens the list of words
    word_list = word_list_file.readlines()
    #word_list = ["Hello", "Greetings", "Salutations", "Somethin", "Else", "Gahhhh"]
    Password = ""

    number_choice = secrets.choice(string.digits)
    symbols_choice = secrets.choice(string.punctuation)

    for i in range(0, word_number):
        next_word = ""
        if include_uppercase == 0:
            next_word = secrets.choice(word_list).strip() 
        else:
            next_word = secrets.choice(word_list).strip()
            
            next_word_list = list(next_word) 

            if uppercase_position - 1 <= len(next_word_list):
                next_word_list[uppercase_position - 1] = next_word_list[uppercase_position - 1].upper()
                next_word = "".join(next_word_list)
            
        if include_numbers == 1:
            if numbers_position - 1 <= len(next_word) and numbers_position - 1 >= 0:
                next_word = next_word[:numbers_position - 1] + number_choice + next_word[numbers_position - 1:]
            
        if include_symbols == 1:
            if symbols_position - 1 <= len(next_word) and symbols_position - 1 >= 0:
                next_word = next_word[:symbols_position - 1] + symbols_choice + next_word[symbols_position - 1:]
                   
        Password = Password + next_word
        
    return Password
