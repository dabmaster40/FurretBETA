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

class playlist(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ET")
    async def _test(self, ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(playlist(bot))