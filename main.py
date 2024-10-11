#working variables for full scope
from more_itertools import split_into


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


def main():
    with open("BookBot/books/frankenstein.txt") as f:
        book_contents = f.read()
    
    word_count_result = word_count(book_contents)
    letter_count_results = letter_count(book_contents)
    print(f"I've Mystically counted {word_count_result} words")
    print(f"I've Majestically counted {letter_count_results} letters")
    "Now lets get fancy, for each character
             There are 0 A's
             There are 0 B's
             There are 0 C's
             There are 0 D's
             There are 0 E's
             There are 0 F's
             There are 0 G's
             There are 0 H's
             There are 0 I's
             There are 0 J's
             There are 0 K's
             There are 0 L's
             There are 0 M's
             There are 0 N's
             There are 0 O's
             There are 0 P's
             There are 0 Q's
             There are 0 R's
             There are 0 S's
             There are 0 T's
             There are 0 U's
             There are 0 V's
             There are 0 W's
             There are 0 X's
             There are 0 Y's
             There are 0 Z's
            all Magnanimously counted"
main()