# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код
def neibors(**kwargs):
    for i in kwargs:
        print('В комнате', i, 'живут:', kwargs[i])


folks_1 = ["Яна", "Алёна", ]
folks_2 = ["Иннокентий Петрович", "Петр Петрович", "Ибрагим"]
folks_3 = ["Рихтер",]

neibors(room_1 = folks_1, room_2 = folks_2, room_3 = folks_3)