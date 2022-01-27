from datetime import datetime
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#StatsCmds===============================================

class embed(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="Stats", description="Stats for Furret aka the nerd command")
    async def stats(self, ctx: SlashContext):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed = Embed(color=0x7289da)
        embed.set_author(
        name="Furret Stats")
        embed.add_field(
        name="Python Version:",
        value=f"3.8",
        inline=True)
        embed.add_field(
        name="Ping:",
        value= f"{round(self.bot.latency * 1000)}ms",
        inline=True)
        embed.add_field(
        name="Bot Uptime:",
        value= f"{days}d, {hours}h, {minutes}m",
        inline=True)
        embed.add_field(
        name="Servers:",
        value= f"{len(self.bot.guilds)}",
        inline=True)
        embed.set_footer(
        text=f"Created by dabmaster40#6556 and Dauhxe#1489")
        await ctx.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(embed(bot))
