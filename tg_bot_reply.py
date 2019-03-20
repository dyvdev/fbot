import random
from textgenrnn import textgenrnn

import telegram.message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


path = 'textgenrnn_weights.hdf5'
botname = 'dyvan_bot'

def echo(update, context):

	if random.random() < 0.2:
		textgen = textgenrnn(path)
		txt = random.choice(update.message.text.split())	
		msg = textgen.generate(n=1, prefix=txt, temperature=0.5, return_as_list=True)
		
		update.message.reply_text(msg[0])
		
def reply(update, context):
	if update.message.text == None:
		return
	if update.message.text.find('?')!= -1:
		textgen = textgenrnn(path)
		msg = textgen.generate(n=1, prefix='ебет тебя? ', temperature=0.5, return_as_list=True)		
		update.message.reply_text(msg[0])
	elif update.message.text.find(botname) != -1 or update.message.text.find(' бот ') != -1 or (update.message.reply_to_message != None and update.message.reply_to_message.from_user.username == botname):
		textgen = textgenrnn(path)
		txt = random.choice(update.message.text.split())	
		msg = textgen.generate(n=1, prefix=txt, temperature=0.5, return_as_list=True)		
		update.message.reply_text(msg[0])
	