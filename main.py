#lets yeet this wheat

print("Welcome to Xerath's word counting compendium")
print("counting words in the tome . . .")
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    count_letters = 0
    for letters in text:
        count_letters += 1
    return count_letters

def per_letter_count(text):
    lower_case = text.lower()
    per_letter = {}
    for letter in lower_case:
        if letter in per_letter:
            per_letter[letter] += 1
        else: 
            per_letter[letter] = 1
    return per_letter

def main():
    with open("BookBot/books/frankenstein.txt") as f:
        book_contents = f.read()
    
    word_count_result = word_count(book_contents)
    letter_count_results = letter_count(book_contents)
    per_letter_count_results = per_letter_count(book_contents)
    print(f"I've Mystically counted {word_count_result} words")
    print(f"I've Majestically counted {letter_count_results} letters")
    print("Now lets get fancy")
    print(per_letter_count_results)
    print("Are you impressed with me?")

if __name__ == "__main__":
    main()