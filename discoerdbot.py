import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='videos'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == 'Hi':
        await client.send_message(message.channel,'Hello.')
    if message.content == '!1273':
        em = discord.Embed(description='')
        em.set_image(url='down the Rockefeller street ')
        await client.send_message(message.channel, embed=em)
    if ('heck') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!memes'):
        randomlist = ['https://cleanmemes.files.wordpress.com/2019/01/img_7510.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7511.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7512.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7513.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7514.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7474.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7478.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7241.jpg']
        await client.send_message(message.channel,(random.choice(randomlist)))


client.run(os.getenv('TOKEN'))
                      
