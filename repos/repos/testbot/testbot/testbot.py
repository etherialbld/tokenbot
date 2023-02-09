import telebot
import sqlite3



TOKEN = '5851633479:AAEZHc0sIgWo4BMMz9rCnOlsiMBMdT7ujV8'
bot = telebot.TeleBot(TOKEN)
res = []
con = sqlite3.connect('olympcodes.db', check_same_thread=False)
cur = con.cursor()


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет, введи свои данные в формате "Фамилия Имя Отчество"')
	cur.execute('INSERT INTO OLYMPCODES (olymptoken, lastname_name_surname) VALUES (?, ?)', (olymptoken, lastname_name_surname))
	con.commit()




@bot.message_handler(content_types=['text'])
def text(message):
	result = cur.execute(f"SELECT olymptoken FROM OLYMPCODES WHERE lastname_name_surname LIKE '{message.text}'")
	olymptoken = result.fetchone()
	con.commit()
	
	if olymptoken == None:
		bot.send_message(message.chat.id, 'Неправильные данные')
	else:
		bot.send_message(message.chat.id, f'Вот твой код: {olymptoken}')























bot.polling()
