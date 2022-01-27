import discord
import os
import DiscordUtils
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

@bot.event #I havent tested this yet so pls dont run the bot with this rn.
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="bot_logs")
    await channel.set_permissions(member, read_messages=False)
    await channel.send(f"Thank you for using Furret.\n If you want Furret to send audit logs, keep this channel and do not change it. Otherwise, disregard.")
    print(Logged.)

#CogCMDS===============================================================

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}...")
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}!")

#PermsCMDS==============================================


#Logging================================================






bot.run('TOKEN')
