#lets yeet this wheat

print("Welcome to Xerath's Word Counting Compendium")
print("counting words in the tome . . .")
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    count_letters = 0
    for letters in text:
        count_letters += 1
    return count_letters

def sort_on(dict):
    return dict['count']

def only_alpha(text):
    only_alpha_text = ""
    for letters in text:
        if letters.isalpha() == True:
            only_alpha_text += letters
    
    return only_alpha_text


def per_letter_count(text):
    #empty variables I need
    
    lower_case = text.lower()
    per_letter = {}
    list_of_per_letter = []
    
    #part 1 make text only alpha

    give_me_alpha = only_alpha(lower_case)

    #part 2 make alpha_text only lowercase, will count occurrences
    
    for letter in give_me_alpha:
        if letter in per_letter:
            per_letter[letter] += 1
        else: 
            per_letter[letter] = 1

    #part 3 big dictionary to list of dictionaries
    for char, count in per_letter.items():
        list_of_per_letter.append({'char': char, 'count': count})
    
    list_of_per_letter.sort(reverse=True, key=sort_on)
    return list_of_per_letter


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
    print("Let me make it pretty for you")
    new_line_counter = 0
    for line in per_letter_count_results:
        if new_line_counter <= 26:
            print(f"Per letter report{per_letter_count_results[new_line_counter]}")
            new_line_counter += 1
    print("This should be easier to read")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("Thank you for using Xerath's Word Counting Compendium")

if __name__ == "__main__":
    main()