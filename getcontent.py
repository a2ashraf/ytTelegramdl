import subprocess
import os
import logging
import youtube_dl
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


token = "401496380:AAEiX7Sv8nsa5WdlLe5MDJbqwpmqptn_i3E"

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger()
bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="Share a URL from Youtube with me, I will send you the vid")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def downloadUrl(bot, input):
    bot.send_message(chat_id=input.message.chat_id, text="Hang on ...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': "%(id)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with ydl:
        result = ydl.extract_info(
            input.message.text,
            download=True  # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    print(video)

    video_title = video['title']
    video_thumbnail = video['thumbnail']
    video_url = video['webpage_url']
    id = video['id']
    ext =  video['ext']
    file_id = open("./"+id+".mp3", "rb")

    # file_id = open("/Users/Ahsan/PycharmProjects/YoutubeDownloader/BaW_jenozKc.mp4", "rb")
    bot.send_message(chat_id=input.message.chat_id, text=video_title)
    bot.send_audio(chat_id=input.message.chat_id, text='a ',audio=file_id)
    file_id.close()

link_handler = MessageHandler(Filters.text, downloadUrl)
dispatcher.add_handler(link_handler )
updater.start_polling()


# class MyLogger(object):
#     def debug(self, msg):
#         pass
#
#     def warning(self, msg):
#         pass
#
#     def error(self, msg):
#         print(msg)


# def my_hook(d):
#     if d['status'] == 'finished':
#         print('Done downloading, now cornverting ...')
#     if d['status'] == 'error':
#         print('Error happend...')
#     if d['status'] == 'downloading':
#         print('currently downloading')

# ydl_opts = {
#     'format': 'bestaudio/best',
#     'verbose':'true',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
#     #'download_archive': '/Users/Ahsan/Desktop/youtubedl/archive.out',
# }


# print(subprocess.check_output(['download.sh','https://www.youtube.com/watch?v=BaW_jenozKc']))

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     # ret_val =  ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
#
#     info_dict = ydl.extract_info("https://www.youtube.com/watch?v=BaW_jenozKc", download=True)
# #    video_url = info_dict.get("url", None)
#     video_id = info_dict.get("id", None)
#  #   video_title = info_dict.get('title', None)
#
#     print("\n" + video_id)










