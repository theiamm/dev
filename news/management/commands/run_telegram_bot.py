import telebot
from django.core.management.base import BaseCommand

from news.models import News


bot = telebot.TeleBot("6341614290:AAHomyyUYSS83IWUqtgOW-jX-XqkS7QSxK4")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['news'])
def news(message):
    all_news = News.objects.all()
    for single_news in all_news:
        news_info = f"{single_news.title}, {single_news.publication_date}"
        bot.send_message(message.chat.id, news_info)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


@bot.message_handler(commands=['add'])
def get_news_title(message):
    bot.send_message(message.chat.id, 'Введите заголовок новостя: ')
    bot.register_next_step_handler(message, get_date)


def get_date(message):
    global news_title
    news_title = message.text
    bot.send_message(message.chat.id, 'Введите дату, например: 2023-06-22 (гггг-мм-дд)')
    bot.register_next_step_handler(message, full_info)


def full_info(message):
    news_date = message.text

    news_post = News(title=news_title, publication_date=news_date)
    news_post.save()

    bot.send_message(message.chat.id, 'Информация была сохранена')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

