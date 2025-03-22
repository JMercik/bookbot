def main():
    from stats import word_count
    num_words = word_count()
    print(f"{num_words} words found in the document")
    
    from stats import character_frequency
    num_characters = character_frequency()
    print(num_characters)
    

if __name__ == "__main__":
    main()

