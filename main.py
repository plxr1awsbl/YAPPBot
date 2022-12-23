import telebot as tb
import answers as ans


bot = tb.TeleBot('5968840553:AAHWXwRKJHWaYPkPzQ-gXG-kntURqBJutvA')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    list1 = ans.content_check(message.text)
    str1 = ans.reply(list1)
    for stR in str1:
        bot.send_message(message.from_user.id, stR)


bot.polling(none_stop=True, interval=0)
