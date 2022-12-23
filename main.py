import telebot as tb
import random as rand

bot = tb.TeleBot('5968840553:AAHWXwRKJHWaYPkPzQ-gXG-kntURqBJutvA')

jokes = ['Генерал: «Здесь шлагбаум, или майора толкового поставить?»',
         'Умер священник. Несут его ангелы к вратам рая, и вдруг вперёд его проносят водителя автобуса. \nСвященник спрашивает: «А почему так?» \nАнгелы ему и говорят: «Ну так у вас на проповедях люди спали, а у водителя в салоне – молились».',
         'Есть люди, в каждой бочке затычка. Они всегда добавят свою бочонок дёгтя в большую ложку мёда.',
         'Городничему надо выдавать дочь замуж. Решил собрать всю знать города, и пригласил дьячка.\nНакрывается стол, гостей ещё нет, а дьячок уже припёрся.\nНакрыли на стол, поставили миску с чёрной икрой. Дьячок взял, и начал есть.\nГородничий у ужасе. Подходит к дьячку, и говорит:\n- Отец дьякон, это же чёрная икра!\n- Икра, икра\n- Отец дьякон, она же стоит рубль!\n- Стоит рубль, да\n- Отец дьякон, её же вредно сразу много есть!\n- А я буду есть её не сразу, а постепенно',
         'У немцев есть такая поговорка: «Любая машина, в конце концов, становится Opel’ем»',
         'Все женщины делятся на дам, не дам;\nДам, но не вам']

hellos_var = ['приветик', 'привет', 'здарова', 'здравствуйте']
wassap_var = ['как дела', 'как делишки']
joke_var =   ['шутку', 'анекдот', 'прикол']
weather_var = ['погода', 'погодку', 'погоду', 'погодка']


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (hellos_var[0] in message.text.lower()) or \
            (hellos_var[1] in message.text.lower()) or \
            (hellos_var[2] in message.text.lower()) or \
            (hellos_var[3] in message.text.lower()):

        bot.send_message(message.from_user.id, 'Ну привет, пользователь')

    if (wassap_var[0] in message.text.lower()) or \
            (wassap_var[1] in message.text.lower()) or \
            (wassap_var[2] in message.text.lower()):

        bot.send_message(message.from_user.id, 'У меня всё отлично, я знаю анекдоты')

    if (joke_var[0] in message.text.lower()) or \
            (joke_var[1] in message.text.lower()) or \
            (joke_var[2] in message.text.lower()):

        joke = jokes[rand.randint(0, 5)]

        bot.send_message(message.from_user.id, joke)

    if (weather_var[0] in message.text.lower()) or \
            (weather_var[1] in message.text.lower()) or \
            (weather_var[2] in message.text.lower()) or \
            (weather_var[3] in message.text.lower()):
        pass