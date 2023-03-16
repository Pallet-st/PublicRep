import telebot
from config import TOKEN, keys
from clasess import ConvertionException, Converter

bot = telebot.TeleBot(TOKEN)







@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту:\n Перевод валют - "<имя валюты> \ <в какую валюту перевести> \ <количество переводимой валюты>;\n Список доступных валют - /values."'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Введено не 3 параметров')
        chto, kuda, kol_vo = values
        t_base = Converter.convert(chto, kuda, kol_vo)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {kol_vo} {chto} - {t_base} {kuda}'
        bot.send_message(message.chat.id, text)


bot.polling()