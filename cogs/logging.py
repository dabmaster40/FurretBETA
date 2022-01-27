from discord import Embed
import discord
import DiscordUtils
from discord.ext.commands import Bot, Cog
from discord.utils import find
from discord.ext import commands
from discord_slash import cog_ext, SlashContext


#==============================================
class logging(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="BotLog", description="Creates bot_log channel")
    async def BotLog(self, ctx: SlashContext):
        guild = ctx.guild
        channel = discord.utils.get(guild.text_channels, name="bot_logs")
        if channel is None:
            await ctx.send("Created bot_logs.")
            channel = await guild.create_text_channel("bot_logs")
            await ctx.message.guild.create_text_channel(channel)
        else:
            await ctx.send("The channel already exists!")

def setup(bot: Bot):
    bot.add_cog(logging(bot))