import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Client
import os

Client = discord.Client()
cl = commands.Bot(command_prefix="$")
cl.run(os.environ['BOT_TOKEN'])


@cl.event
async def on_ready():
    
  online_message = 'deploying to cloud...'
  print (online_message)
    
      
@cl.event
async def on_message(message):

  msg = message.content
  print(msg)
  
