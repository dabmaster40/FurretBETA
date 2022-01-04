from random import choice
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class bye(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Bye', description = 'Says bye')
    async def stats(self, ctx: SlashContext):
        responses = ['finally', 'cya', 'oh ok....']
        await ctx.send(choice(responses))

def setup(bot: Bot):
    bot.add_cog(bye(bot))
