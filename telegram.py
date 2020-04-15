import telebot
import pyowm
from telebot import types
import random

owm = pyowm.OWM("905c95dc8f833e9035b8f633fc478ee6", language = "ru")

bot = telebot.TeleBot("1147580820:AAHaQFebkCXVYcgzJsaBsch_kt8YD0sZx_Q")

hi = ["Привет!", "Как делишки?", "Давно не виделись)", "Приветсвую", "Рад тебя видеть!)", "Здравствуй!"]

cold = ["шапку", " теплую куртку", "джинсы"]

mormal = ["кепку", "ветровку", "джинсы"]

hot = ["кепку", "футболку", "легкие джинсы или шорты"]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, random.choice(hi))
    bot.reply_to(message, "Вот, что я умею: \n --- Пиши 'Погода'")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "погода" == (message.text).lower():
        bot.send_message(message.from_user.id, "Какой населенный пункт тебе нужен?")
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, "Я отвечаю только на вопросы о погоде)")
        
@bot.message_handler(content_types=['text'])
def get_weather(message):
    global place
    place = (message.text).lower()
    global w
    try:
        observation = owm.weather_at_place(place)
        
        w = observation.get_weather()

        temp = w.get_temperature('celsius')["temp"]

        bot.send_message(message.from_user.id, "Сейчас на улице: " + w.get_detailed_status() + " " + str(round(temp)) + "°C")
        
        if temp <= 0:
            bot.send_message(message.from_user.id, "На улице холодно. Думаю тебе стоит одеть" + cold[0] + ", сверху" + cold[1] + "и" + cold[2])
        elif temp > 0 and temp <= 16:
            bot.send_message(message.from_user.id, "На улице холодно. Думаю тебе стоит одеть" + normal[0] + ", сверху" + normal[1] + "и" + normal[2])
        elif temp > 16:
            bot.send_message(message.from_user.id, "На улице холодно. Думаю тебе стоит одеть" + hot[0] + ", сверху" + hot[1] + "и" + hot[2])
 
        bot.send_message(message.from_user.id, "Хочешь узнать подробности? Если хочешь пиши 'Подробности'")
        
        bot.register_next_step_handler(message, get_weather_detailed)
    except:

        bot.send_message(message.from_user.id, "Прости, но я не нашел информацию по населенному пунктку '" + place + "'")
        
@bot.message_handler(content_types=['text'])
def get_weather_detailed(message):

    if (message.text).lower() == "да":
        try:
            bot.send_message(message.from_user.id, "Скорость ветра: " + str(w.get_wind()["speed"]) + " м/с")
            
            bot.send_message(message.from_user.id, "Влажность воздуха: " + str(w.get_humidity()) + "%")
            
        except:
            bot.send_message(message.from_user.id, "Что-то пошло не так(")
        
bot.polling(none_stop=True, interval=0)
