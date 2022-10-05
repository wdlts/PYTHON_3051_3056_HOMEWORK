from pytube import YouTube


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}.mp4')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}.mp4', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='*Вот ваше видео*', parse_mode='Markdown')


async def download_youtube_audio(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True)
    stream.get_audio_only().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}.mp3')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}.mp3', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio, caption='*Вот ваше аудио*', parse_mode='Markdown')
