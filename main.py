def main():
    from stats import word_count
    num_words = word_count()
    print(f"{num_words} words found in the document")
    

if __name__ == "__main__":
    main()

