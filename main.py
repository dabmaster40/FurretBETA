import discord
import os


from discord.ext import commands
from discord_slash import SlashCommand
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = '<')
slash = SlashCommand(bot, sync_commands=True)
intents = discord.Intents.all()
sent_users = []
bot.launch_time = datetime.utcnow()
#Bot==Events==================================================================

@bot.event
async def on_ready():
  print('Furret is ready')
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        print(f"Joined {guild.name}")
  print('----------------------------------------------------')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))

  

#Import==Commands===============================================================

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}...")
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}!")

#Economy=====================================================================



#Permission==Required==Commands==============================================






bot.run('TOKEN')
