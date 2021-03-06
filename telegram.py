import telebot
import pyowm
from telebot import types
import random

owm = pyowm.OWM("905c95dc8f833e9035b8f633fc478ee6", language = "ru") #подключаем api openweather

bot = telebot.TeleBot("1147580820:AAHaQFebkCXVYcgzJsaBsch_kt8YD0sZx_Q") #подключаем api telegram

#подготавливаем фразы
hi = ["Привет!", "Как делишки?", "Давно не виделись)", "Приветсвую", "Рад тебя видеть!)", "Здравствуй!"]

cold = [" шапку", " теплую куртку", " джинсы"]

normal = [" кепку", " ветровку", " джинсы"]

hot = [" кепку", " футболку", " легкие джинсы или шорты"]


#функция ответа на команды
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, random.choice(hi))
    bot.reply_to(message, "Вот, что я умею: \n --- Пиши 'Погода'")


#функция ответа на текстовое сообщение
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if "погода" == (message.text).lower():
        bot.send_message(message.from_user.id, "Какой населенный пункт тебя интересует?")
        bot.register_next_step_handler(message, get_weather)
    else:
        bot.send_message(message.from_user.id, "Я отвечаю только на вопросы о погоде)")
  

#функция, выполняемая при запросе "погода"
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
            bot.send_message(message.from_user.id, "На улице холодно. Думаю тебе стоит надеть" + cold[0] + ", сверху" + cold[1] + " и" + cold[2])
        elif temp > 0 and temp <= 16:
            bot.send_message(message.from_user.id, "На улице прохоладно. Думаю тебе стоит надеть" + normal[0] + ", сверху" + normal[1] + " и" + normal[2])
        elif temp > 16 and temp <= 23:
            bot.send_message(message.from_user.id, "На улице тепло. Думаю тебе стоит надеть" + hot[0] + ", сверху" + hot[1] + " и" + hot[2])
        elif temp > 23:
            bot.send_message(message.from_user.id, "На улице жарко. Думаю стоит просто надеть легкую одежду. Не забудь головной убор!")
 
        bot.send_message(message.from_user.id, "Хочешь узнать подробности? Если хочешь пиши 'Подробности'")
        
        bot.register_next_step_handler(message, get_weather_detailed)
        
    except:

        bot.send_message(message.from_user.id, "Прости, но я не нашел информацию по населенному пунктку '" + place + "'")
        
        
#функция, выполняемая при запросе "погода"-"подробности"
@bot.message_handler(content_types=['text'])
def get_weather_detailed(message):

    if (message.text).lower() == "подробности":
        try:
            bot.send_message(message.from_user.id, "Скорость ветра: " + str(w.get_wind()["speed"]) + " м/с")
            
            bot.send_message(message.from_user.id, "Влажность воздуха: " + str(w.get_humidity()) + "%")
            
            bot.send_message(message.from_user.id, "Больше информации здесь: https://yandex.ru/pogoda")
            
        except:
            bot.send_message(message.from_user.id, "Что-то пошло не так(")
    else:
        bot.send_message(message.from_user.id, "Прости, но я тебя не понял")
        bot.register_next_step_handler(message, get_text_messages)
        
bot.polling(none_stop=True, interval=0)
