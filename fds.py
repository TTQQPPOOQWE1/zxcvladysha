import asyncio
from telegram import Bot
from telegram.error import TelegramError

TOKEN = '8075152649:AAHywEVGS5y4dJlbdOEG3XyHYR4_OukFT7M'        # Замени на токен от @BotFather
CHAT_ID = -1002727869944        # Замени на ID группы (с минусом)

bot = Bot(token=TOKEN)

async def send_mut_every_5_minutes():
    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text="мут")
        except TelegramError as e:
            print(f"Ошибка при отправке: {e}")
        await asyncio.sleep(300)  # 300 секунд = 5 минут

if __name__ == "__main__":
    asyncio.run(send_mut_every_5_minutes())
