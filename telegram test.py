import telegram
import schedule
import time
import datetime
import asyncio
import pytz

# 텔레그램 봇 설정
token = "6736572403:AAFqSX_mS5AyGZ0c5bSHP4bmtBvJ_MLWtrE"
bot = telegram.Bot(token=token)
mychat = '6633530090'
public_chat_name = "@K2019test"

# 메시지를 보내는 함수
def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

    asyncio.get_event_loop().run_until_complete(send(str(now)))

async def send(time):
    await bot.sendMessage(chat_id=public_chat_name, text=time)
    print(f"Sent message: ", time)

schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)