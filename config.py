
def put_in_db(msgid, first, last, userus):
    userid = 'id: ' + str(msgid)
    if str(first) != 'None':
        userfname = ' name: ' + str(first)
    else:
        userfname = ''
    if str(last) != 'None':
        userlname = ' ' + str(last)
    else:
        userlname = ''
    useruser = ' username: @' + str(userus)

    users = open("users.txt", "a")
    users.write(userid)
    users.write(userfname)
    users.write(userlname)
    users.write(useruser)
    users.write("\n")
    users.close()

def put_in_db_dai(msgid, first, last, userus, hour, minute):
    userid = 'id: ' + str(msgid)
    if str(first) != 'None':
        userfname = ' name: ' + str(first)
    else:
        userfname = ''
    if str(last) != 'None':
        userlname = ' ' + str(last)
    else:
        userlname = ''
    useruser = ' username: @' + str(userus)

    user = open("usersdai.txt", "a")
    user.write(str(hour) + ':' + str(minute) + ' ')
    user.write(userid)
    user.write(userfname)
    user.write(userlname)
    user.write(useruser)
    user.write("\n")
    user.close()

para = ['Дискретная математика (лекция)\n\nСтатус: можно поспать',       # 0
        'Дискретная математика (практика)\n\nСтатус: можно поспать',     # 1
        'Программирование (лекция)\n\nСтатус: можно поспать',            # 2
        'Программирование (практика)\n\nСтатус: можно поспать',          # 3
        'Английский язык (практика)\n\nСтатус: нельзя поспать',          # 4
        'История (лекция)\n\nСтатус: можно поспать',                     # 5
        'История (практика)\n\nСтатус: нельзя поспать',                  # 6
        'БЖД (лекция)\n\nСтатус: можно поспать',                         # 7
        'БЖД (практика)\n\nСтатус: нельзя поспать',                      # 8
        'Чеченская культура и этика (лекция)\n\nСтатус: можно поспать',  # 9
        'История ЧР (лекция)\n\nСтатус: можно поспать',                  # 10
        'Мат. анализ (лекция)\n\nСтатус: можно поспать',                 # 11
        'Мат. анализ (практика)\n\nСтатус: можно поспать',               # 12
        'Теория вероятностей (практика)\n\nСтатус: можно поспать',       # 13
        'Введение в ПИ (лекция)\n\nСтатус: можно поспать',               # 14
        'Введение в ПИ (практика)\n\nСтатус: можно поспать']             # 15

raspisanie = 'BQACAgIAAxkDAAICPl64er94NiYxab2Vu5aCMe1nx5QQAAIGCgACC4nASfd25oHvfjAkGQQ'

salam = """Ассаламу алейкум\n
Я - Дистанционка БОТ группы ПИ-1💻\n
Что я умею:
✅Выдавать ссылку на трансляцию Webex, которая идёт в настоящий момент
✅Показывать расписание всех пар\n
Чтобы начать, выбери номер своей подгруппы, нажав одну из кнопок ниже"""

no_podgrupp = """По всей видимости, ты не указал номер своей подгруппы.\n
Нажми кнопку <i>\"Начать сначала\"</i> и следуй дальнейшим инструкциям."""

chill = 'В данный момент времени пар нет. Отдыхай :)'

spisok = """[Программирование](https://chesuru.webex.com/meet/a.khotov)\n
[Введение в ПИ](https://chesuru.webex.com/meet/minaevosman)\n
[История](https://chesuru.webex.com/meet/hatmat73)\n
[БЖД](https://chesuru.webex.com/meet/yusupu)\n
[Математический Анализ](https://chesuru.webex.com/meet/aldymadina537)\n
[Теория Вероятностей](https://chesuru.webex.com/meet/zaya310387)\n
[Дискретная Математика](https://chesuru.webex.com/meet/magomerzaev57)\n
[История ЧР](https://chesuru.webex.com/meet/nataev.s)\n
[Чеченская Культура и Этика](https://chesuru.webex.com/meet/sbeguev)\n 
[Английский 1 подгр](https://chesuru.webex.com/meet/elinastar.ru)\n 
[Английский 2 подгр](https://chesuru.webex.com/meet/star1918)"""

helpp = """Чтобы получить ссылку, нажми кнопку  <i>\"Дай ссылку\"</i>
\nЧтобы получить полный список ссылок на трансляции, нажми кнопку <i>\"Полный список пар\"</i>
\nЧтобы получить расписание всех пар, нажми кнопку <i>\"Расписание\"</i>
\nЧтобы начать заново, нажми кнопку <i>\"Начать сначала\"</i>"""
