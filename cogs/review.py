from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class review(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Review', description = 'Links the top.gg page for Furret')
    async def review(self, ctx: SlashContext):
        embed = Embed(title='Like Furret?', description= 'Please review Furret here!' + "(https://top.gg/bot/884858660935827467)".format(self.bot.user.id))
        await ctx.send(embed=embed)

def setup(bot: Bot):
    bot.add_cog(review(bot))
