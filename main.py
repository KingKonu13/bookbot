def main():
    with open("/Users/michaelkonu/workspace2/github.com/KingKonu13/bookbot/books/frankenstein.txt") as f:
        file_content = f.read()
    counter = 0 
    
    def counts_number_of_words_in_books(book):
        list_of_words_in_book = book.split()
        return len(list_of_words_in_book)
        
    print(counts_number_of_words_in_books(file_content))

main()