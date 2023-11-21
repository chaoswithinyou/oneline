import telebot
from newsplease import NewsPlease


def get_text_old(url):
    try:
        article = NewsPlease.from_url(url)
        try:
            fulltext = (
                article.title + ". " + article.description + ". " + article.maintext
            )
        except Exception:
            try:
                fulltext = article.title + ". " + article.maintext
            except Exception:
                fulltext = article.maintext
        if len(fulltext) < 100:
            return "Error 1"
        return fulltext
    except Exception:
        return "Error 2"


def get_text(url):
    article = NewsPlease.from_url(url)
    fulltext = article.maintext
    if fulltext:
        return fulltext
    else:
        return "Lỗi: không đọc được tin bài."


class quickbot:
    def __init__(self, api_key, input_function):
        self.api_key = api_key
        self.bot = telebot.TeleBot(self.api_key)
        self.input_function = input_function

        @self.bot.message_handler(commands=["url"])
        def url(message):
            input_text = get_text(message.text[5:])
            self.bot.send_message(message.chat.id, str(self.input_function(input_text)))

        @self.bot.message_handler(commands=["text"])
        def text(message):
            self.bot.send_message(
                message.chat.id, str(self.input_function(message.text[6:]))
            )

    def run(self, timeout=10, long_polling_timeout=5):
        self.bot.infinity_polling(
            timeout=timeout, long_polling_timeout=long_polling_timeout
        )
