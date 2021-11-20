# Напишите view-функцию, которая позволит 
# с помощью запроса на адрес /search/ с параметром
# city произвести поиск города по вхождению
# искомой строки в название города.
# Регистр при этом не учитывать.
# Результат необходимо вывести через запятую.
# Например:
#
# * При запросе на адрес: /search/?city=са
#   на странице необходимо отобразить результат:
#   Санкт-Петербург, Самара, Саратов
#
# * При запросе на адрес: /search/ без параметров
#   отобразить сообщение "Введите параметр city"
#
# * А если ничего найти не удалось тогда вывести текст
#   Городов не найдено.
#
# В данном задании язык html-разметки использовать не нужно.
#
# Также не стоит делать сортировку запроса. При тестировании 
# Вашего решения будет использоваться тот порядок выдачи,
# по которому сейчас отсортирован имеющийся список.
# 

from flask import Flask, request
app = # TODO инициализируйте приложение здесь

locations = [
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Екатеринбург",
    "Казань",
    "Нижний Новгород",
    "Челябинск",
    "Самара",
    "Омск",
    "Ростов-на-Дону",
    "Уфа",
    "Красноярск",
    "Воронеж",
    "Пермь",
    "Волгоград",
    "Краснодар",
    "Волгоград",
    "Саратов",
    "Тюмень",
    "Тольятти",
    "Ижевск",
]


# TODO напишите view-функцию здесь


if __name__ == '__main__':
    app.run()