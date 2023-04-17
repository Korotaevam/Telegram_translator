import time

from aiogram import Bot, Dispatcher, executor, types
import logging

from aiogram.types import ContentType

from translator import lingvo_translator
from secret_token import Translator_Bot_Token

TOKEN = Translator_Bot_Token
MSG = '{}, какое слово перевести? поменять язык? набери "-revers-"'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

from_what = [1049, 'Русский']
on_which = [1033, 'English']

# @dp.message_handler(commands=['start'])

@dp.message_handler()
async def conversation_handlers(message: types.Message):


    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f'{user_id=} {user_full_name}  {time.asctime()}')

    translate_word = message["text"]

    if translate_word.strip() == '-revers-':
        global from_what, on_which
        from_what, on_which = on_which, from_what
        await message.reply(f'язык поменял {from_what[1]}-{on_which[1]}')

    else:
        translated_word = lingvo_translator(translate_word, from_what[0], on_which[0])
        await message.reply(f'{translate_word} - {translated_word}')
        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)
