#working variables for full scope
print("Welcome to Xerath's word counting compendium")
print("counting words in the tome . . .")
def word_count(text):
    words = text.split()
    return len(words)


def main():
    with open("BookBot/books/frankenstein.txt") as f:
        book_contents = f.read()
    
    word_count_result = word_count(book_contents)
    print(f"I've counted {word_count_result} words")
main()