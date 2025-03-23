def main():
    from stats import (
        word_count,
        character_frequency,
        sorted_cha,
    )
    
    def get_book_path(path):
        with open(path) as f:
            return f.read()

    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = word_count(text)
    sorted_cha_list = sorted_cha(text)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for entry in sorted_cha_list:
        print(f"{entry["cha"]}: {entry["num"]}")

    print("============= END ===============")

    

if __name__ == "__main__":
    main()

