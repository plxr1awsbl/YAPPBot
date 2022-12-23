import telebot as tb
import answers as ans


bot = tb.TeleBot('5968840553:AAHWXwRKJHWaYPkPzQ-gXG-kntURqBJutvA')
stickers = ['CAACAgIAAxkBAAEG-UdjpgEAAScAAROl75EPxSPLtmVo77UKAAJbPAAC6VUFGFRHApuJ0sb7LAQ',
            'CAACAgIAAxkBAAEG-UljpgEHBTNWEDavSo-yGWrE2Yz99QACXDwAAulVBRgHO15I9c2NVSwE',
            'CAACAgIAAxkBAAEG-UtjpgG5bUJiHU7QQ4lArhX3VG3gOAACajwAAulVBRixL0lTfWHQaywE',
            'CAACAgIAAxkBAAEG-U1jpgHX3gvTuFtNpgXDmHItmCnqtQACwR4AAoJCkEq7SCx2G7aiTiwE',
            'CAACAgIAAxkBAAEG-U9jpgHqRGRzxDDmn3PEUKNs1LDCDQACPhUAAuE7yEshrvTovPQkDywE']

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, 'Я могу рассказывать анекдоты, отвечать как дела и здороваться, на не текстовые сообщения кидаю стикеры')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    list1 = ans.content_check(message.text)
    str1 = ans.reply(list1)
    for stR in str1:
        bot.send_message(message.from_user.id, stR)


@bot.message_handler(content_types=['sticker', 'photo', 'video', 'audio'])
def get_sticker(message):
    bot.send_sticker(message.from_user.id, stickers[ans.rand.randint(0, 4)])


bot.polling(none_stop=True, interval=0)
