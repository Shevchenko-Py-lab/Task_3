from random import shuffle


def get_jokes(jokes_quantity, repeats):
    """
    Составитель шуток на основе случайно создаваемого списка

    :param jokes_quantity: количество шуток
    :param repeats: с повторами, или без (по умолчанию любой символ не "Y" означает без повторов)
    :return: joke_list - составленные шутки
    """
    i = 0
    k = 5
    joke_list = []

    if jokes_quantity <= 0:
        print("Без шуток")
    else:
        while i < jokes_quantity:
            r = list(range(k))
            shuffle(r)
            if repeats == "Y":
                joke = nouns[r[0]] + " " + adverbs[r[1]] + " " + adjectives[r[2]]
                joke_list.append(joke)
            else:
                if jokes_quantity > 5:
                    jokes_quantity = 5
                    print("Без повторов больше пяти шуток не выдать")
                joke = nouns[r[0]] + " " + adverbs[r[0]] + " " + adjectives[r[0]]
                joke_list.append(joke)
                nouns.pop(r[0])
                adverbs.pop(r[0])
                adjectives.pop(r[0])
                k -= 1
            i += 1

        return joke_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

n = int(input("Введите количество шуток "))
rep = input("Использовать повторы слов? Y - с повторами слов ")
print(get_jokes(n, rep))

