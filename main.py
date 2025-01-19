def main():
    with open("books/frankenstein.txt") as txt:
        file_contents = txt.read()
    
    print(word_counter(file_contents))

def word_counter(data):

    words = data.split()
    counter_dict = {}
    character_list = []

    for characters in words:
        for character in characters:
            character_list.append(character.lower())
            counter_dict[character.lower()] = 0
    
    for letters in character_list:
        if letters in counter_dict:
            counter_dict[letters] += 1

    return counter_dict
main()

