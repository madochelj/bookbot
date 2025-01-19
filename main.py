def main():
    with open("books/frankenstein.txt") as txt:
        file_contents = txt.read()
    
    print(word_counter(file_contents))

def word_counter(data):

    words = data.split()
    counter_dict = {'p': 0, 'c': 0, ' ':0}
    character_list = []

    for num in range(0, len(data)):
        character_list.append(data[num].lower())

    for letters in character_list:
        if letters in counter_dict:
            counter_dict[letters] += 1

    return counter_dict
main()

