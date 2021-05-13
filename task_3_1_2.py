def num_translate_adv():
    word_to_translate = input("Введите слово для перевода: ")
    word_to_translate = str(word_to_translate)
    for letter in word_to_translate[0]:
        if letter.islower():
            translate = word_number.get(word_to_translate, 'Слова нет в словаре')
            print(translate)
        else:
            word_to_translate = str.lower(word_to_translate)
            translate = word_number.get(word_to_translate, 'Слова нет в словаре')
            print(translate.capitalize())


word_number = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num_translate_adv()