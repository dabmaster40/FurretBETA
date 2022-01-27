import discord
import os
import DiscordUtils
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#==============================================================================

class logging(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        deleted = Embed(description=f"Message deleted in {message.channel.mention}"
        ).set_author(name=message.author, url=Embed.Empty, icon_url=message.author.avatar_url)
        deleted.add_field(name="Message", value=message.content)
        deleted.timestamp = message.created_at
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_message_edit(message_before, message_after):
        edited = Embed(description=f"Message edited in {message_before.channel.mention}").set_author(
        name=message_before.author.name, url=Embed.Empty, icon_url=message_before.author.avatar_url)
        channel = discord.utils.get(message_before.guild.text_channels, name='bot_logs')
        edited.add_field(name="Message before", value=message_before.content)
        edited.add_field(name="Message after", value=message_after.content)
        edited.timestamp = message_before.created_at
        await channel.send(embed=edited)

    @commands.Cog.listener()
    async def on_member_update(before, after):
        if len(before.roles) < len(after.roles):
            rc = Embed(title=f"{before.name} roles changed.")
            channel = discord.utils.get(before.guild.text_channels, name='bot_logs')
            rc.add_field(name="Updated Role List", value=after.roles)
            await channel.send(embed=rc)

#more cog listeners here...

def setup(bot: Bot):
    bot.add_cog(embed(bot))