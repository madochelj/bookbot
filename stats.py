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
