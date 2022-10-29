#1.
def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()

    dict_ = {}

    for simbol in str_:
        if simbol.isalpha():
            if simbol in dict_:
                dict_[simbol] += 1
            else:
                dict_[simbol] = 1
    return dict_

#5.
def get_procent(dict_):
    dict_.keys()
    for key in dict_:
        dict_[key] = round(dict_[key] * 100 / sum(dict_.values()))
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_procent(get_count_char(main_str)))