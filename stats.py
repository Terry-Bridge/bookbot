def get_word_count(file):
    with open(file) as f:
        contents = f.read()
        words = contents.split()
    return f"Found {len(words)} total words"
    

def get_char_count(file):
    character_count = {}
    with open(file) as f:
        contents = f.read().lower()
        words = contents.split()
        
        for word in words:
            for letter in word:
                if letter not in character_count:
                    character_count[letter] = 1
                else:
                    character_count[letter] += 1

    return character_count


def get_value(dict):
    return list(dict.values())[0]

def char_count_formatted(dict):
    dict_as_list = []
    for k, v in dict.items():
        if k.isalpha():
            dict_as_list.append({k:v})
    dict_as_list.sort(reverse=True, key=get_value)


    for i in range(len(dict_as_list)):
        for k, v in dict_as_list[i].items():
            print(f"{k}: {v}")

    
    
            