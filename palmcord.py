import asyncio
import discord
from discord.ext import commands

bot = commands.Bot("prefixL ", self_bot=True)

@bot.event
async def on_ready():
    print("check 1 passed")

@bot.command()
async def messagething(msg):
    await msg.send("heres your discord link") ### to send a message when message thing is said.

bot.run("your token", bot=False)
