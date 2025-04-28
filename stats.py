def num_of_words(text):
    num_word = len(text.split())
    return num_word

def num_of_char(text):
    lower_case_text = text.lower()
    dicx = {}
    for i in lower_case_text:
        if i in dicx:
            dicx[i] += 1
        else:
            dicx[i] = 1
    return dicx

def chars_dict_to_sorted_list(char_count):
    chars_list = [{"char": char, "num": count} for char, count in char_count.items()]
    chars_list.sort(reverse=True, key=lambda d: d["num"])
    return chars_list
    



