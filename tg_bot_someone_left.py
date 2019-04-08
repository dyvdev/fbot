import telegram.message
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def chatleft(update, context):
	update.message.reply_text(update.effective_user + ' just left')
	
def main():
	updater = Updater(tele_token, use_context=True)
	dp = updater.dispatcher
	
	dp.add_handler(MessageHandler(Filters.status_update.left_chat_member, chatleft))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()