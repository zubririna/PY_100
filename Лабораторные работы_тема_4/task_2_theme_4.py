def get_count_char(str_):
    letter_dict = {}
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# функция, принимающая словарь символов и возващающая их процентное отношение

def give_proc(dict_)
    sum_let = 0
    for letter in dict_:
        sum_let += dict_[letter]
    for letter in dict_:
        dict_[letter] = dict_[letter] / sum_let * 100
    return dict_