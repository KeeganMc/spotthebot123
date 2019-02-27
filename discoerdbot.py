import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '=help':
        await client.send_message(message.channel,'``meme , help , prefix , info , bot``')
    if message.content == '=':
        await client.send_message(message.channel,'Invalid command')
    if message.content == '=prefix':
        await client.send_message(message.channel,'``=``')
    if message.content == '=info':
        await client.send_message(message.channel,'This bot was made by Rogue0730')
    if ('heck') in message.content:
       await client.delete_message(message)
    if message.content.startswith('=meme'):
        randomlist = ['https://cleanmemes.files.wordpress.com/2019/01/img_7555.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7556.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7557.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7558.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7559.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7560.jpg','https://cleanmemes.files.wordpress.com/2019/01/img_7550.jpg']
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run(os.getenv('TOKEN'))
