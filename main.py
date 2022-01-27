import discord
import os
import DiscordUtils
import asyncio
from discord import Embed
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
  print('Furret is ready')
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        print(f"Joined {guild.name}")
  print('----------------------------------------------------')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))

#CogCMDS===============================================================

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}...")
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}!")

#PermsCMDS==============================================


#Logging================================================

@bot.listener()
async def on_guild_join(guild): #DOES NOT WORK YET LMAOOOOOO
    channel = discord.utils.get(guild.text_channels, name="bot_logs")
    if channel.name == "bot_logs":
        return
    else:
        await guild.create_text_channel("bot_logs")
        await channel.send(f"Thank you for inviting Furret! \n Feel free to delete this channel if you do not want me to print audit logs here.")


#=========================================================
bot.run('TOKEN')
