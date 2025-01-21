def main():
    with open("books/frankenstein.txt") as txt:
        file_contents = txt.read()
    
    dic_count = word_counter(file_contents)
    #Thsi function is only here for the acitveity in boot.dev report function is more complete an functional
    activity(dict_to_list_convert(word_counter(file_contents)))
    #report(dic_count, file_contents)

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
    print(f"{word_count} words found in the document\n")
    proper_list = dict_to_list_convert(dic)

    for num in range(1, len(proper_list)):
        temp_dict = proper_list[num]
        if temp_dict["char"].isalpha():
            print(f"The {temp_dict['char']} was found {temp_dict['Value']} times")
    print("--- End report ---")

# convert a dictionary into a list of dictionarys
def dict_to_list_convert(dict):
    dtol = [{"char":k, "Value":v} for k,v in dict.items()]
    dtol.sort(key=lambda dtol: dtol["Value"], reverse=True)
    return dtol

def activity(data):
    for entry in data:
        if entry["char"] == 'e':
            char = (entry["char"])
            print(f"'{char}'")
            print(entry["Value"])
        if entry["char"] == 'n':
            char2 = (entry["char"])
            print(f"'{char2}'")
            print(entry["Value"])

main()

