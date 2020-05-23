import json

def put_in_object(user_id, user_firstName, user_lastName, username):

    if user_lastName is None:
        user_lastName = ''
    if username is None:
        username = 'null'

    dump_json_template = {
        "ID: ": user_id,
        "Name: ": user_firstName + " " + user_lastName,
        "Username: ": "@" + username
    }

    dump_json_template_ToJson = {
        "UserData": dump_json_template
    }

    with open("UserHistoryData.json", "a", encoding="UTF-8") as jsonUserDataFile:
        jsonUserDataFile.write(json.dumps(dump_json_template_ToJson))
        jsonUserDataFile.write("\n")

def get_discipline(index):
    with open("disciplines.json", "r", encoding="utf-8") as jsonFile:
        data = json.loads(jsonFile.read())
        data_index = data["{}".format(index)]
        if data_index[2] == "yes":
            return "{}\t({})\n\n{}".format(data_index[0], data_index[1], "Можно спать")
        elif data_index[2] == "no":
            return "{}\t({})\n\n{}".format(data_index[0], data_index[1], "Спать нельзя")
        elif data_index[2] == "break":
            return "{}\n\n{}".format(data_index[0], "Можно спать")

raspisanie = 'BQACAgIAAxkDAAIUw17JIqz3uShgEQ7R-CynGamc2b3iAAKmBgACT_dISry8ZIIFkm7lGQQ'

salaam = """Ассаламу алейкум\n
Я - Дистанционка БОТ группы ПИ-1💻\n
Что я умею:
✅Выдавать ссылку на трансляцию Webex, которая идёт в настоящий момент
✅Показывать расписание всех пар\n
Чтобы начать, выбери номер своей подгруппы, нажав одну из кнопок ниже"""

no_subgroup = """По всей видимости, ты не указал номер своей подгруппы.\n
Нажми кнопку <i>\"Начать сначала\"</i> и следуй дальнейшим инструкциям."""

chill = 'В данный момент времени пар нет. Отдыхай :)'

help = """Чтобы получить ссылку, нажми кнопку  <i>\"Дай ссылку\"</i>
\nЧтобы получить полный список ссылок на трансляции, нажми кнопку <i>\"Полный список пар\"</i>
\nЧтобы получить расписание всех пар, нажми кнопку <i>\"Расписание\"</i>
\nЧтобы начать заново, нажми кнопку <i>\"Начать сначала\"</i>"""
