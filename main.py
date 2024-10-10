def main():
    with open("BookBot/books/frankenstein.txt") as f:
        # . . .
        print("im picking a book")
        book_contents = f.read()

main()

print("im done reading")
