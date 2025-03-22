#use title path to return full text
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text_contents = f.read()
    return text_contents

def word_count():
    book_text = get_book_text()
    text_list = book_text.split()
    count = 0

    for word in text_list:
        count += 1
    
    return count


def main():
    num_words = word_count()
    print(f"{num_words} words found in the document")
    

if __name__ == "__main__":
    main()

