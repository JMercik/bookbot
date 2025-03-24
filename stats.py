#use title path to return full text
def get_book_text(text_path):
    with open(text_path) as f:
        text_contents = f.read()
    return text_contents

#use get_book_text to count words
def word_count(text_path):
    book_text = get_book_text(text_path)
    text_list = book_text.split()
    count = 0

    for word in text_list:
        count += 1
    
    return count

#use get_book_text to find the frequency of characters
def character_frequency(text_path):
    book_text = get_book_text(text_path).lower()
    character_dictionary = {}
    
    for cha in book_text:
        
        if (cha in character_dictionary) == False:
            character_dictionary[cha] = 0
        character_dictionary[cha] += 1
        
    return character_dictionary

#create a book report from word_count and character_frequency
def sorted_cha(text_path):
    sorted_dict = character_frequency(text_path)
    list_sorted = []
    
    def sort_on(dict):
        return dict["num"]

    for cha in sorted_dict:
        if cha.isalpha() == True:
            list_sorted.append({"cha": cha, "num": sorted_dict[cha]})
    
    list_sorted.sort(reverse=True, key=sort_on)

    return list_sorted
