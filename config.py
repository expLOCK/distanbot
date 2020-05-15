import json


def put_in_object(user_id, user_firstName, user_lastName, username):
    dump_json_template = {
        "ID: ": user_id,
        "First name: ": user_firstName,
        "Last name: ": user_lastName,
        "Username: ": "@" + username
    }

    dump_json_template_ToJson = {
        "UserData": dump_json_template
    }

    with open("UserHistoryData.json", "a", encoding="UTF-8") as jsonUserDataFile:
        jsonUserDataFile.write(json.dumps(dump_json_template_ToJson))
        jsonUserDataFile.write("\n")


raspisanie = 'BQACAgIAAxkDAAICPl64er94NiYxab2Vu5aCMe1nx5QQAAIGCgACC4nASfd25oHvfjAkGQQ'

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
