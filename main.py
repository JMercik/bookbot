def main():
    from stats import word_count
    num_words = word_count()

    from stats import character_frequency
    
    from stats import sorted_cha
    sorted_cha_list = sorted_cha()

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for entry in sorted_cha_list:
        print(f"{entry["cha"]}: {entry["num"]}")

    print("============= END ===============")

    

if __name__ == "__main__":
    main()

