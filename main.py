import discord
import os
import aiohttp
import asyncio
import random
import json
import praw


from discord.ext import commands, tasks
from discord_slash import SlashCommand
from datetime import datetime
from discord import Embed
from discord import Member, Role
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from random import choice

bot = commands.Bot(command_prefix = '<')
slash = SlashCommand(bot, sync_commands=True)
intents = discord.Intents.all()
sent_users = []
bot.launch_time = datetime.utcnow()
bot.load_extension('cogs.embed')
bot.load_extension('cogs.playlist')
bot.load_extension('cogs.support')
#Bot==Events==================================================================

@bot.event
async def on_ready():
  print('Furret is ready')
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        print(f"Joined {guild.name}")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))

  

#Basic==Commands===============================================================


#Economy=====================================================================



#Permission==Required==Commands==============================================






bot.run('OTI2NjMxNzI5NTEzNTI1MzEx.Yc-fDA.Kbh13EpnTV3ybLaTWfTILQt6dRE')
