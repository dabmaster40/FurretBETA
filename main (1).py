import discord
import os
import aiohttp
import asyncio
import random
import json
import praw
import aiofiles


from discord.ext import commands
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
bot.remove_command("help")
bot.launch_time = datetime.utcnow()

#Bot==Events==================================================================

@bot.event
async def on_ready():
  print('Furret is ready')
  print(f'Furret is in {len(bot.guilds)} server(s)!')
  for guild in bot.guilds:
        print("Joined {}".format(guild.name))



#Basic==Commands===============================================================

@slash.slash(name = 'Meme', description = 'Sends a meme from r/memes')
@commands.cooldown(1, 2, commands.BucketType.user)
async def meme(ctx):
  await ctx.send("One second...")
  reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                      client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                      user_agent='script by dabmaster_40')

  submission = reddit.subreddit("memes").random()
  await ctx.send(submission.url)

@slash.slash(name = 'Cat', description = 'Sends a cat from r/catpictures')
@commands.cooldown(1, 2, commands.BucketType.user)
async def cat(ctx):
  await ctx.send("One second...")
  reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                      client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                      user_agent='script by dabmaster_40')

  submission = reddit.subreddit("catpictures").random()
  await ctx.send(submission.url)

@slash.slash(name = 'Dog', description = 'Sends a dog from r/dogpictures')
@commands.cooldown(1, 2, commands.BucketType.user)
async def dog(ctx):
  await ctx.send("One second...")
  reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                      client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                      user_agent='script by dabmaster_40')
  submission = reddit.subreddit("dogpictures").random()
  await ctx.send(submission.url)

@slash.slash(name = 'Review', description = 'Links the top.gg page for Furret')
@commands.cooldown(1, 2, commands.BucketType.user)
async def review(ctx):
  embed = discord.Embed(title='Like Furret?', description= 'Please review Furret here!' + "(https://top.gg/bot/884858660935827467)".format(bot.user.id))
  await ctx.send(embed=embed)

@slash.slash(name = 'Hello', description = 'Says hello')
@commands.cooldown(1, 2, commands.BucketType.user)
async def hello(ctx):
  responses = [
    '***grumble*** Why did you wake me up?', 'Hewwo uwu', '***z z z z z***', 'Hello, how are you?', 'Hi', '**...pardon?**', 'Hi! My names furret!', '***__Why are we still here...just to suffer?__***', ''
    ]
  await ctx.send(choice(responses))
    
@slash.slash(name = 'Bye', description = 'Says bye')
@commands.cooldown(1, 2, commands.BucketType.user)
async def bye(ctx):
  responses = ['finally', 'cya', 'oh ok....']
  await ctx.send(choice(responses))


#Economy=====================================================================



#Permission==Required==Commands==============================================

bot.run('OTI2NjMxNzI5NTEzNTI1MzEx.Yc-fDA.7WUTAbr8G1Evrfhjr8kjM8AXvX8')