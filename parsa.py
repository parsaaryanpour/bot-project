from pyrogram import Client, filters
from yt_dlp import YoutubeDL
from pyrogram.types import Message
import os
# مث
bot_token = 'bot token'
api_id = "api id"
api_hash = "api hash"
bot = Client("YoutubeDL", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@bot.on_message(filters.command(["send480", "send720","start"]) & filters.private)
def download_ytub(c,msg:Message):
    if msg.text == "/start":
        return msg.reply_text("سلام به ربات ما خوش آمدید برای دریافت ربات با کیفیت مورد نظر از دستورات پایین استفاده کنید.\n\n/send480\n\n/send720",quote=True)
    try:
        url = msg.text.split()[1]
        if "/send480" in msg.text:
            desired_format = "480"
        elif "/send720" in msg.text:
            desired_format = "720"
        ydl_opts = {
            'format': f'best[height={desired_format}]',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
        
        
        video_file = f"{info_dict['title']}.mp4"
        print(video_file)
        msg.reply_video(video_file)
        
        os.remove(video_file)
        
    except Exception as e:
        if "Requested format is not available." in str(e):
            return msg.reply_text( f"کیفیت وارد شده برای لینک مورد نظر وجود ندارد !")
        msg.reply_text( f"خطا: {str(e)}")


bot.run()