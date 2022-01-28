import discord
import os
import DiscordUtils
import asyncio
from discord import Embed
from discord.utils import find
from discord.ext import commands
from discord_slash import SlashCommand
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = '<')
slash = SlashCommand(bot, sync_commands=True)
intents = discord.Intents.all()
sent_users = []
bot.launch_time = datetime.utcnow()
#BotEvent==================================================================

@bot.event
async def on_ready():
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        print(f"Joined {guild.name}")
  print('----------------------------------------------------')
  print('   ___________                           __\n  ',
        '\_   _____/_ ________________   _____/  |_\n ',
        '  |    __)|  |  \_  __ \_  __ \_/ __ \   __\ \n',
        '   |     \ |  |  /|  | \/|  | \/\  ___/|  |\n  ',
        ' \___  / |____/ |__|   |__|    \___  >__| \n ',
        '     \/                            \/ \n      ')
  print('----------------------------------------------------')
  print('Furret is online with all cogs loaded. 2022')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))

#CogCMDS===============================================================

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}...")
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}!")

#MusicLoader==============================================


#Logging================================================


#=========================================================
bot.run('')
