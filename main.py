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

#Logging=========================================================

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    deleted = Embed(
        description=f"Message deleted in {message.channel.mention}").set_author(name=message.author, url=Embed.Empty,
                                                                                icon_url=message.author.avatar_url)
    channel = discord.utils.get(message.guild.text_channels, name='bot_logs')
    deleted.add_field(name="Message deleted", value=message.content)
    deleted.timestamp = message.created_at
    await channel.send(embed=deleted)

@bot.event
async def on_message_edit(message_before, message_after):
    edited = Embed(
        description=f"Message edited in {message_before.channel.mention}").set_author(name=message_before.author.name,
                                                                                      url=Embed.Empty,
                                                                                      icon_url=message_before.author.avatar_url)
    channel = discord.utils.get(message_before.guild.text_channels, name='bot_logs')
    edited.add_field(name="Message before", value=message_before.content)
    edited.add_field(name="Message after", value=message_after.content)
    edited.timestamp = message_before.created_at
    await channel.send(embed=edited)

@bot.event
async def on_guild_role_create(role):
    await asyncio.sleep(10)
    channel = discord.utils.get(role.guild.text_channels, name='bot_logs')
    guild = bot.get_guild(357275687989673984)
    rc = discord.Embed(title=f"**New role created**", description=f"{role.mention}", timestamp=role.created_at)
    await channel.send(embed=rc)

@bot.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
        guild = bot.get_guild(357275687989673984)
        ru = discord.Embed(title="Role " + before.name + " changed to " + after.name + ".")
        await channel.send(embed=ru)

@bot.event
async def on_guild_role_delete(role):
    await asyncio.sleep(10)
    channel = discord.utils.get(role.guild.text_channels, name='bot_logs')
    guild = bot.get_guild(357275687989673984)
    rd = discord.Embed(title=f"**Role deleted**", description=f"{role.mention}", timestamp=role.created_at)
    await channel.send(embed=rd)

@bot.event
async def on_guild_channel_create(before):
    cc = Embed(description=f"{before.name}"
    ).set_author(name=f"New channel was created.")
    channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
    guild = bot.get_guild(357275687989673984)
    await channel.send(embed=cc)

@bot.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
        guild = bot.get_guild(357275687989673984)
        cu = discord.Embed(title="Channel " + before.name + " renamed to " + after.name + ".")
        await channel.send(embed=cu)

@bot.event
async def on_guild_channel_delete(before):
    await asyncio.sleep(10)
    channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
    guild = bot.get_guild(357275687989673984)
    cd = discord.Embed(title=f"**Channel deleted**", description=f"{before.name}")
    await channel.send(embed=cd)

@bot.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        rc = Embed(title=f"{before.name} roles changed.")
        channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
        rc.add_field(name="Updated Role List", value=after.roles)
        await channel.send(embed=rc)

#================================================================

bot.run(config.BOT_TOKEN, bot=True, reconnect=True)
