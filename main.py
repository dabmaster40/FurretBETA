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
from config import config
from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot import utils
from musicbot.utils import guild_to_audiocontroller, guild_to_settings
from musicbot.commands.general import General

#===============================================================================

intents = discord.Intents.all()
initial_extensions = ['musicbot.commands.music',
                      'musicbot.commands.general', 'musicbot.plugins.button']
bot = commands.Bot(command_prefix=config.BOT_PREFIX,
                   pm_help=True, case_insensitive=True, intents = intents)
slash = SlashCommand(bot, sync_commands=True)
sent_users = []
bot.launch_time = datetime.utcnow()

if __name__ == '__main__':

    config.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    config.COOKIE_PATH = config.ABSOLUTE_PATH + config.COOKIE_PATH

    if config.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)

#BotEvents========================================================================================

@bot.event
async def on_ready():
  print('Furret is ready')
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        await register(guild)
        print(f"Joined {guild.name}")
  print('----------------------------------------------------')
  print('   ___________                           __\n  ',
        '\_   _____/_ ________________   _____/  |_\n ',
        '  |    __)|  |  \_  __ \_  __ \_/ __ \   __\ \n',
        '   |     \ |  |  /|  | \/|  | \/\  ___/|  |\n  ',
        ' \___  / |____/ |__|   |__|    \___  >__| \n ',
        '      \/                            \/ \n      ')
  print('----------------------------------------------------')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers"))
  print(config.STARTUP_COMPLETE_MESSAGE)

#OnGuildJoin===========================================================

@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)

async def register(guild):
    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)
    sett = guild_to_settings[guild]
    try:
        await guild.me.edit(nick=sett.get('default_nickname'))
    except:
        return
    if config.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return
    vc_channels = guild.voice_channels
    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)
        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)

#CogCMDS===============================================================

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading {filename}...")
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded {filename}!")

#=========================================================

bot.run(config.BOT_TOKEN, bot=True, reconnect=True)
