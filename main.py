def main():
    with open("books/frankenstein.txt") as txt:
        file_contents = txt.read()
    
    dic_count = word_counter(file_contents)
    report(dic_count, file_contents)
    print(dict_to_list_convert(dic_count))

def word_counter(data):

    words = data.split()
    counter_dict = {}
    character_list = []

    for num in range(0, len(data)):
        character_list.append(data[num].lower())
        counter_dict[data[num].lower()] = 0

    for letters in character_list:
        if letters in counter_dict:
            counter_dict[letters] += 1

    return counter_dict

def report(dic, data):
    print("--- Begin report of books/frankenstein.txt ---")
    words = data.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
    print("\n")

# convert a dictionary into a list of dictionarys
def dict_to_list_convert(dict):
    dtol = [{"char":k, "Value":v} for k,v in dict.items()]
    dtol.sort(key=lambda dtol: dtol["Value"])
    return dtol
main()

