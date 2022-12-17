from configparser import ConfigParser 
from pyrogram import Client
from pyrogram import filters
import dbot

config = ConfigParser()

config.read('config.ini')

api_id = config.get('pyrogram', 'api_id')
api_hash = config.get('pyrogram', 'api_hash')

app = Client('my_account', api_id = api_id, api_hash = api_hash)

@app.on_message(filters.private)
async def auto_answer(event, message):
	if  message.from_user.id == (await app.get_me()).id:
		pass
	else:
		check = dbot.register_user(message.chat.id)
		if check == 'None': 
			await app.send_message(message.chat.id, text='Добрый день, меня зовут Ирина. Подскажите, какое изделие Вас заинтересовало?\n\nСможете прислать ссылку? Или Вам нужна консультация?')
		elif check == 'second':
			await app.send_message(message.chat.id, text='Связываю Вас с менеджером!')
		elif check == 'third':
			await app.send_message(message.chat.id, text='Пожалуйста подождите!')
		else:
			pass

app.run()