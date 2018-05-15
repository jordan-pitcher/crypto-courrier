import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Client
from coinmarketcap import Market
import os

Client = discord.Client()
cl = commands.Bot(command_prefix="$")
cl.run(os.environ['BOT_TOKEN'])
coinmarketcap = Market()

'''
display the top crypto currency stats from coinmarketcap
'''

@cl.command(pass_context=True)
@commands.cooldown(1, 60, commands.BucketType.user) 
async def top(ctx, cnt):
     
    coin_stats = coinmarketcap.ticker(limit=cnt)
    await cl.say(f"Displaying top {cnt} crypto currencies from CoinMarketCap")

    

@cl.event
async def on_ready():
    
  online_message = 'deploying to cloud...'
  print (online_message)
    
      
@cl.event
async def on_message(message):

  msg = message.content
  print(msg)
  
