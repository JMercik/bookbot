#use title path to return full text
def get_book_text():
    with open("books/frankenstein.txt") as f:
        text_contents = f.read()
    return text_contents


def main():
    book_text = get_book_text()
    print(book_text)

if __name__ == "__main__":
    main()

