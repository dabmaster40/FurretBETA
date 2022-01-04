from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class support(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Support', description = 'Sends a link to Furret\'s Support Server')
    async def support(ctx):
        await ctx.send(f"Click below to go to Furret's Support Server!")
        await ctx.send(f"https://discord.gg/8vscBHSNqA")

def setup(bot: Bot):
    bot.add_cog(support(bot))