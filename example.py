import discord
from discord.ext import commands 
                
client = commands.Bot(comand_prefix='!') # you can choose your own prefix here
                
@client.event()
async def on_ready():
  print(f"Bot online and logged in as {client.user}")
                
# a simple command
@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
                
client.run('your token here') # running the bot
