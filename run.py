import asyncio
from telethon import TelegramClient, events


api_id = ""
api_hash = ''
bot_token = ''

bot = TelegramClient('test_bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hi')
    
@bot.on(events.NewMessage(pattern='!ping'))
async def handler(event):
    m = await event.reply('!pong')
    print(event)
    await asyncio.sleep(5)
    await bot.delete_messages(event.chat_id, [event.id, m.id])


def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
