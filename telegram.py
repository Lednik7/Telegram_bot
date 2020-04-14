import telebot

bot = telebot.TeleBot("1147580820:AAHaQFebkCXVYcgzJsaBsch_kt8YD0sZx_Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.lower() == "погода":
        print("yES")

bot.polling()
