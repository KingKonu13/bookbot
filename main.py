def main():
    with open("/Users/michaelkonu/workspace2/github.com/KingKonu13/bookbot/books/frankenstein.txt") as f:
        file_content = f.read()
    counter = 0 
    
    def counts_number_of_words_in_books(book):
        list_of_words_in_book = book.split()
        return len(list_of_words_in_book)
        
    # print(counts_number_of_words_in_books(file_content))
    
    def chars_counter(text):
        table_of_chars = {}
        for char in text:
            char = char.lower()
            if char in table_of_chars:
                table_of_chars[char] += 1 
            else:
                table_of_chars[char] = 1
        return table_of_chars
        

    print(chars_counter(file_content))
    
    def report_generator(words, table):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print()

        for key,value in table.items():
            print(f"The {key} charachter was found {value} times")
        print("--- End report ---")
        
    report_generator(counts_number_of_words_in_books(file_content), chars_counter(file_content))
main()