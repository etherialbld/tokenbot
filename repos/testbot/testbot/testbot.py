import telebot
import sqlite3



TOKEN = '5851633479:AAEZHc0sIgWo4BMMz9rCnOlsiMBMdT7ujV8'
bot = telebot.TeleBot(TOKEN)
res = []

@bot.message_handler(commands=['start'])
def start(message):
	con = sqlite3.connect('olympcodes.db')
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS login_id(
		id INTEGER 
	)""")
	con.commit()

	user_id = [message.chat.id]
	cur.execute("INSERT INTO login_id VALUES(?);", user_id)
	con.commit()

	res = cur.execute("SELECT id FROM login_id")
	con.commit()


	USER_FIRST_NAME = message.from_user.first_name
	bot.send_message(message.chat.id, f'Привет, {USER_FIRST_NAME}, выбери предмет:')

@bot.message_handler(content_types=['text'])
def text(message):
	if message.text.lower() == 'id':
		bot.send_message(message.chat.id, res)
















bot.polling()
