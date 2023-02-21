import telebot
from telebot import types

bot = telebot.TeleBot("6228470981:AAHjgM9Pny67lRvTCv8WlW2ilTvR_4DmuPc")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет, чем помочь Вашему питомцу?")

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", url="https://groomik.ru"))
    bot.send_message(message.chat.id, text="Нажмите кнопку", reply_markup=markup)

@bot.message_handler(commands=['telegram'])
def telegram(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в Телеграм", url="https://t.me/groomiktut"))
    bot.send_message(message.chat.id, text="Нажмите кнопку", reply_markup=markup)


@bot.message_handler(commands=['vk'])
def vk(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти в VK", url="https://vk.com/groomik"))
    bot.send_message(message.chat.id, text="Нажмите кнопку", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "уход за животными":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Стрижка кошек')
        btn2 = types.KeyboardButton('Стрижка собак')
        btn3 = types.KeyboardButton('Ультразвуковая чистка зубов')
        btn4 = types.KeyboardButton('Экспресс-линька')
        btn5 = types.KeyboardButton('Выставочный груминг мейн-куна')
        markup.add(btn1,btn2,btn3,btn4,btn5)
        final_message = "Пожалуйста, выберите услугу:"

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Стрижка кошек')
        btn2 = types.KeyboardButton('Стрижка собак')
        btn3 = types.KeyboardButton('Ультразвуковая чистка зубов')
        btn4 = types.KeyboardButton('Экспресс-линька')
        btn5 = types.KeyboardButton('Выставочный груминг мейн-куна')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        final_message = "Ой, что-то не то. Нажмите на кнопки ниже"
    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

