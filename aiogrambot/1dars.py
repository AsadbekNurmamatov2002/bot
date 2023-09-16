import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
#bot TOKEN joylaymiz

bot=Bot(token="6629607723:AAGG8mpv6N1tFQzDOmlPW9ZjN3FluNUNZNQ")
dp=Dispatcher()
#command start
@dp.message(F.text=='/start')
async def cmd_start(message:Message):
    await message.answer('Salom')

async def main():
    await dp.start_polling(bot)
if __name__=='__main__':
    asyncio.run(main())
