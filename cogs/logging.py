from discord import Embed
from discord.ext.commands import Bot, Cog
from discord.utils import find
from discord.ext import commands


#==============================================
class logging(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, ctx, guild):
        await ctx.create_text_channel('bot_logs')
        bl = find(lambda x: x.name == 'bot_logs', guild.text_channels)
        if bl and bl.permissions_for(guild.me).send_messages:
            await ctx.send(
                f"Hello {guild.name}!! Thank you for inviting Furret!!.\n Feel free to delete this channel if you do not want me to print audit logs in this server.")



def setup(bot: Bot):
    bot.add_cog(logging(bot))