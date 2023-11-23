import telegram
import schedule
import time
import datetime
import asyncio
import pytz

# 텔레그램 봇 설정
token = "Your_token"
bot = telegram.Bot(token=token)
mychat = 'bot_chatid'
public_chat_name = "@K2019test"

# 메시지를 보내는 함수
def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
# 오후 11시 부터 아침 6시까지는 메시지 출력 금지    
    if now.hour >= 23 or now.hour <= 6:
        return

    asyncio.get_event_loop().run_until_complete(send(str(now)))

async def send(time):
    await bot.sendMessage(chat_id=public_chat_name, text=time)
    print(f"Sent message: ", time)

# 30분 단위로 개설 채널에 메세지 전송
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
