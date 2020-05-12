
raspisanie = 'id файла с расписанием'

salam = """Ассаламу алейкум\n
Я - Дистанционка БОТ группы ПИ-1💻\n
Что я умею:
✅Выдавать ссылку на трансляцию Webex, которая идёт в настоящий момент
✅Показывать расписание всех пар\n
Чтобы начать, выбери номер своей подгруппы, нажав одну из кнопок ниже"""

no_podgrupp = """По всей видимости, ты не указал номер своей подгруппы.\n
Нажми кнопку <i>\"Начать сначала\"</i> и следуй дальнейшим инструкциям."""

chill = 'В данный момент времени пар нет. Отдыхай :)'

link = 'Ссылка на пару:'

spisok = """[Программирование](https://chesuru.webex.com/meet/)\n
[Введение в ПИ](https://chesuru.webex.com/meet/)\n
[История](https://chesuru.webex.com/meet/)\n
[БЖД](https://chesuru.webex.com/meet/)\n
[Математический Анализ](https://chesuru.webex.com/meet/)\n
[Теория Вероятностей](https://chesuru.webex.com/meet/)\n
[Дискретная Математика](https://chesuru.webex.com/meet/)\n
[История ЧР](https://chesuru.webex.com/meet/)\n
[Чеченская Культура и Этика](https://chesuru.webex.com/meet/)\n 
[Английский 1 подгр](https://chesuru.webex.com/meet/)\n 
[Английский 2 подгр](https://chesuru.webex.com/meet/)"""

helpp = """Чтобы получить ссылку, нажми кнопку  <i>\"Дай ссылку\"</i>
\nЧтобы получить полный список ссылок на трансляции, нажми кнопку <i>\"Полный список пар\"</i>
\nЧтобы получить расписание всех пар, нажми кнопку <i>\"Расписание\"</i>
\nЧтобы начать заново, нажми кнопку <i>\"Начать сначала\"</i>"""

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
