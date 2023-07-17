import telebot
from telebot import util
from newsplease import NewsPlease
import jsonlines


def get_text(url):
    try:
        article = NewsPlease.from_url(url)
        try:
            fulltext = article.title + '. ' + article.description + '. ' + article.maintext
        except Exception:
            try:
                fulltext = article.title + '. ' + article.maintext
            except Exception:
                fulltext = article.maintext
        if len(fulltext) < 100:
            return 'Error 1'
        return fulltext
    except Exception:
        return 'Error 2'


class quickbot:
    def __init__(self, api_key, input_function):
        self.api_key = api_key
        self.bot = telebot.TeleBot(self.api_key)
        self.input_function = input_function
        
        @self.bot.message_handler(commands=['url'])
        def url(message):
            input_text = get_text(message.text[5:])
            self.bot.send_message(message.chat.id, str(self.input_function(input_text)))
        
        @self.bot.message_handler(commands=['text'])
        def text(message):
            self.bot.send_message(message.chat.id, str(self.input_function(message.text[6:])))

    def run(self, timeout=10, long_polling_timeout=5):
        self.bot.infinity_polling(timeout=timeout, long_polling_timeout=long_polling_timeout)


class labelbot:
    def __init__(self, api_key, jsonl_input_dir, jsonl_output_dir, highlight_function=None):
        self.api_key = api_key
        self.bot = telebot.TeleBot(self.api_key)
        self.highlight_function = highlight_function
        self.texts = []
        self.done_count = 0
        self.current_count = 0
        
        try:
            with jsonlines.open(jsonl_output_dir) as reader:
                for article in reader:
                    self.done_count += 1
        except Exception:
            pass

        with jsonlines.open(jsonl_input_dir) as reader:
            for article in reader:
                if self.done_count > 0:
                    self.done_count -= 1
                    continue
                self.texts.append(article['text'])
        
        @self.bot.message_handler(commands=['a'])
        def a(message):
            if self.current_count == len(self.texts):
                self.bot.send_message(message.chat.id, 'No more samples left.')
            else:
                self.current_text = self.texts[self.current_count]
                self.bot.send_message(message.chat.id, str(self.current_count))
                if self.highlight_function != None:
                    splitted_text = util.smart_split(self.highlight_function(self.current_text), chars_per_string=2000)
                else:
                    splitted_text = util.smart_split(self.current_text, chars_per_string=2000)
                for text in splitted_text:
                    self.bot.send_message(message.chat.id, text)
                self.current_count += 1
        
        @self.bot.message_handler(commands=['b'])
        def b(message):
            label_text = get_text(message.text[3:])
            try:
                with jsonlines.open(jsonl_output_dir, mode='a') as writer:
                    writer.write({'text':self.current_text, 'label_text':label_text})
                self.bot.send_message(message.chat.id, f'{str(self.current_count)} done.')
            except Exception:
                self.bot.send_message(message.chat.id, 'Something went wrong.')
            

    def run(self, timeout=10, long_polling_timeout=5):
        self.bot.infinity_polling(timeout=timeout, long_polling_timeout=long_polling_timeout)


class highlight_text:
    def __init__(self, highlight_list):
        self.highlight_list = highlight_list
    def __call__(self, text):
        count = 1
        for obj in self.highlight_list:
            if obj in text:
                text = text.replace(obj, "*<" + str(count) + "> " + obj + '*')
                count += 1
        return text
