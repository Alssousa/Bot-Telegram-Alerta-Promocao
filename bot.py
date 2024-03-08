from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, Message
from dotenv import load_dotenv
from os import getenv
from scraping import acessar_produto


load_dotenv()

app = Client("promocaoalertabot", api_id=getenv('TELEGRAM_API_ID'), api_hash=getenv('TELEGRAM_API_HASH'), bot_token=getenv('TELEGRAM_BOT_TOKEN'))

#Inicialmente recebe qualquer link e verifica se o codigo tem compatibilidade com o site, para retornar se é possivel o monitoramento.
@app.on_message()
async def no_command(client, message: Message):
    await message.reply(f'Olá {message.from_user.first_name}, iniciarei o monitoramento do produto desejado :D.')
    produto = acessar_produto(message.text)
    if produto:
        await app.send_message(message.chat.id, f'O produto monitorado é: {produto}')
    else:
        await app.send_message(message.chat.id, f'Por favor, forneça um link válido no formato - https://xxxx.xxx/xxxxxxx')

    

app.run()