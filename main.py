import discord
import os
import time
import random
from discord.ext import commands
from discord.ext.commands import Bot

token = "TOKEN" #YOUR SELFBOT TOKEN (NOT A BOT!!!)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='k!', intents=intents, self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd)
    print('logged in as {0.user}'.format(bot))

@bot.event
async def on_ready():
    l = [955184672265109564, 955184671086489611, 843239436303990814, 955184669995958413, 958530233278017606, 985930766997413938] #CHANNEL IDS WHERE YOU WANT TO STEAL THE ICONS FROM
    while True:
        channel = bot.get_channel((random.choice(l)))
        async for message in channel.history():
            content = message.attachments
            for i in content:
                channel = bot.get_channel(985887858952908841) #CHANNEL ID TO POST THE ICONS 
                time.sleep(5)
                await channel.send(i) 

bot.run(token, bot=False)
