import telebot
from telebot import types
import requests

class UrlCat(telebot.TeleBot):

    url: str = "https://cataas.com/cat"
    text: str = str()

    def __init__(self, token: str):
        super().__init__(token)
    
    def __send_welcome(self, message: types.Message) -> None:
        self.__markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        self.__btn1 = types.KeyboardButton("cat")
        self.__btn2 = types.KeyboardButton("cute cat")
        self.__btn3 = types.KeyboardButton("cat with text")
        self.__markup.add(self.__btn1, self.__btn2, self.__btn3)

        self.send_message(message.from_user.id, "Выбери котика", reply_markup=self.__markup)


    def __get_text_messages(self, message: types.Message) -> None:
        if message.text == 'cat':
            self.url = "https://cataas.com/cat"
            self.__send_photo(message)
        elif message.text == "cute cat":
            self.url = "https://cataas.com/cat/cute"
            self.__send_photo(message)
        elif message.text == "cat with text":
            self.url = "https://cataas.com/cat/says/"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Отправить текст")
            btn2 = types.KeyboardButton("Назад")
            markup.add(btn1, btn2)
            self.send_message(message.from_user.id, "Прими решение", reply_markup=markup)
        elif message.text == "Отправить текст":
            self.url += self.text
            self.__send_photo(message)
        elif message.text == "Назад":
            self.__send_welcome(message)
        else:
            self.text = message.text

    def __send_photo(self, message) -> None:
        response = requests.get(self.url)
        photo = response.content
        self.send_photo(message.chat.id, photo)
        self.text = ""
        self.__send_welcome(message)

    def run(self):
        self.register_message_handler(self.__send_welcome, commands=['start'])
        self.register_message_handler(self.__get_text_messages, content_types=['text'])
        self.polling(none_stop=True, interval=0)

def main():
    bot = UrlCat("7176599287:AAEMPIUNICI0bN1FhNg4NsiVjY1ijF9kFDU")
    bot.run()

if __name__ == "__main__":
    main()
