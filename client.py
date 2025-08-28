from telethon import TelegramClient, events, sync
from config import API_ID, API_HASH, SESSION_NAME, DEFAULT_RECIPIENT, DEFAULT_FILE_PATH

# Client is now configured using values from config.py
client = TelegramClient('session_name', api_id, api_hash)
client.start()


print(client.get_me().stringify())

client.send_message('username', 'Hello! Talking to you from Telethon')
client.send_file('username', '/home/myself/Pictures/holidays.jpg')

client.download_profile_photo('me')
messages = client.get_messages('username')
messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')
