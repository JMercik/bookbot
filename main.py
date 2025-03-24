def main():
    import sys
    from stats import (
        word_count,
        #character_frequency,
        sorted_cha,
    )
    
    def get_book_path(path):
        with open(path) as f:
            return f.read()
    
    #check if file path was supplied to main
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    book_path = sys.argv[1]
    #text = get_book_path(book_path)
    num_words = word_count(book_path)
    sorted_cha_list = sorted_cha(book_path)


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

