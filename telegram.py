import telebot
import pyowm

owm = pyowm.OWM("905c95dc8f833e9035b8f633fc478ee6", language = "ru")

bot = telebot.TeleBot("1147580820:AAHaQFebkCXVYcgzJsaBsch_kt8YD0sZx_Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Вот, что я умею: \n ---Пиши 'погода {название населенного пункта}'")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "погода" in (message.text).lower():
        place = (message.text).lower()
        try:
            place = place[place.find(" ")+1:]
            
            observation = owm.weather_at_place(place)

            w = observation.get_weather()

            temp = w.get_temperature('celsius')["temp"]

            bot.send_message(message.from_user.id, "Сейчас на улице: " + w.get_detailed_status(), str(round(temp)) + "°C")
            bot.send_message(message.from_user.id, "Скорость ветра: " + str(w.get_wind()["speed"]) + " м/с")
            bot.send_message(message.from_user.id, "Влажность воздуха: " + str(w.get_humidity()) + "%")
            
            bot.send_message(message.from_user.id, "Обращайся, если хочешь узнать погоду)")

        except:

            bot.send_message(message.from_user.id, "Прости, но я не нашел информацию по населенному пунктку '" + place + "'")
            
@bot.message_handler(content_types=['text'])
def random_text():
    bot.send_message(message.from_user.id, "Обращайся по погоде)"
        
bot.polling(none_stop=True, interval=0)

