from aiogram import *
from pytube import YouTube
from keys import download_youtube_video
from keys import download_youtube_audio

bot = Bot('YOUR_TOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['video'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Скачаю видео и аудио, вставьте ссылку ")


@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'*Начинаю скачивать* : {yt.title}', parse_mode='Markdown')
        await download_youtube_video(url, message, bot)
        await download_youtube_audio(url, message, bot)


if __name__ == '__main__':
    executor.start_polling(dp)
