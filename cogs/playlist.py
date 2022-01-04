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
import wavelink
import itertools
import re


from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class Bot(Bot):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=['audio ', 'wave ','aw '])

        self.add_cog(playlist(self))

    async def on_ready(self):
        print(f'Logged in as {self.user.name} | {self.user.id}')


class playlist(Cog):

    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        await self.bot.wavelink.initiate_node(host='173.249.9.178',
                                              port=5074,
                                              rest_uri='http://173.249.9.178:5074',
                                              password='EpikHostOnTop',
                                              identifier='TEST',
                                              region='us_central')

    @cog_ext.cog_slash(name='connect')
    async def connect_(self, ctx: SlashContext, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(f'Connecting to **`{channel.name}`**')
        await player.connect(channel.id)

    @cog_ext.cog_slash()
    async def play(self, ctx: SlashContext, *, query: str):
        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

        if not tracks:
            return await ctx.send('Could not find any songs with that query.')

        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        await ctx.send(f'Added {str(tracks[0])} to the queue.')
        await player.play(tracks[0])

def setup(bot: Bot):
    bot.add_cog(playlist(bot))
