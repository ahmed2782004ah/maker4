from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="25336226",
    api_hash="fc6670f0d2070c0a6defb9c25b92c384",
    bot_token="6477407510:AAHdX4kXIH3CILzRFFhhBgvKgrOkruYXuqc",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "IIUll_l"
    await bot.send_message(AFROTOO, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
