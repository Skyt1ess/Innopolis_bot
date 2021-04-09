from peewee import SqliteDatabase

TOKEN = "1673153242:AAFpK743DUx_eVBvEQsvYRZUISlOsoVNczs"
DB = SqliteDatabase('database.db')
admins = ['skytless1']
deadline = '22:00 МСК'

def get_question_chat_id():
    f = open('question_chat_id', 'r')
    for line in f:
        question_chat_id = line.strip('\n')
    f.close()
    return question_chat_id


def set_question_chat_id(chat_id):
    f = open('question_chat_id', 'w')
    f.write(str(chat_id))
    f.close()


help_user = 'Каждое утро ПН-СБ вы будете получать ссылку на задачу.\n' \
            'За час до дедлайна бот пришлет уведомление о том, что нужно сдать задачу.\n' \
            f'в {deadline} вы получите ссылку на разбор задачи.\n\n' \
            'Вы можете задать любой вопрос с помощью команды:\n' \
            '/question вопрос\n' \
            'Мы постараемся ответить на него как можно скорее!'

help_admin = 'Список команд:\n' \
             '/add_users - добавляет список пользователей.\n' \
             '/add_course - добавляет курс.\n' \
             '/print_course - выводит информацию о курсе.\n' \
             '/show_courses - показывает все курсы.\n' \
             '/delete_course - удаляет курс.\n\n' \
             'Чтобы узнать подробнее о команде - введите\n' \
             '/info command_name\n' \
             'Например: /info add_users'
