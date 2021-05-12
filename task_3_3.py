# После долгих боёв с 3, 4 я не осилил

def thesaurus(name):

    def name_letters(employee_names):
        """Составление списка ключей первых букв имён"""
        key_list = []
        for letter in employee_names:
            capital_letter = chr(ord((letter[0])))
            key_list.append(capital_letter)
            counter = key_list.count(capital_letter)
            if counter > 1:
                key_list.pop()
            key_list.sort()
        return key_list

    def name_filter(elem):
        """Фильтр по первым буквам имён"""
        return elem.startswith(k)

    list_names = name_letters(name)
    list_check = []
    for k in list_names:
        employee_name_filter = list(filter(name_filter, name))
        list_check.append(employee_name_filter)
        list_check.sort()

    my_dict = dict(zip(list_names, list_check))

    return my_dict


employee_name = ["Иван", "Мария", "Петр", "Илья", "Василий", "Виталий"]

dict_print = dict(thesaurus(employee_name))
print(dict_print)
