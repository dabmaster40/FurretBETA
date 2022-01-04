import discord
import os
import aiohttp
import asyncio
import random
import json
import praw
import aiofiles
from typing import Union
import sys
import traceback
import humanize
import itertools
import re


from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class embed(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="Stats", description="Stats for Furret aka the nerd command")
    async def stats(self, ctx: SlashContext):
        embed = Embed(title="Bot Stats", description="Created by dabmaster40#6556 with help from Dauhxe#1489")
        await ctx.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(embed(bot))
