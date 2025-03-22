#use title path to return full text
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text_contents = f.read()
    return text_contents

#use get_book_text to count words
def word_count():
    book_text = get_book_text()
    text_list = book_text.split()
    count = 0

    for word in text_list:
        count += 1
    
    return count

#use get_book_text to find the frequency of characters
def character_frequency():
    book_text = get_book_text().lower()
    character_dictionary = {}
    
    for cha in book_text:
        
        if (cha in character_dictionary) == False:
            character_dictionary[cha] = 0
        character_dictionary[cha] += 1
        
    return character_dictionary
