# MarrckxBot.py
from lib2to3.pgen2 import token
from operator import truediv
import os
import random
from aiohttp import ClientError
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members =True

    
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT')
GUILD = os.getenv('DISCORD_GUILD')

MarckxBot = commands.Bot(command_prefix='>',intents=intents) 

@MarckxBot.event
async def on_ready():

    Servidor = discord.utils.find(lambda Server: Server.name == GUILD, MarckxBot.guilds)

    print(
        f'\n {MarckxBot.user} Acabo de depertar Sr.Coronado.\n'
        f'\n Estoy disponible en el: {Servidor.name} ( id: {Servidor.id})'
    )
    \
    '''
    Usuarios_Server = '\n - '.join([Usuarios_Server.name for Usuarios_Server in Servidor.members])
    print(f'\n Usuarios en el servidor: \n - {Usuarios_Server}')

    '''  
@MarckxBot.command(name = "Hola Marck")
async def prueba(ctx):
    response = "Hola Sr.Coronado, acabo de nacer"
    await ctx.send(response)

@MarckxBot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise   

MarckxBot.run(TOKEN)

