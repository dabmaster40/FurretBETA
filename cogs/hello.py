from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext
from random import choice

#Playlist==Commands===============================================

class embed(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Hello', description = 'Says hello')
    async def stats(self, ctx: SlashContext):
        responses = [
            '***grumble*** Why did you wake me up?', 'Hewwo uwu', '***z z z z z***', 'Hello, how are you?', 'Hi', '**...pardon?**', 'Hi! My names furret!', '***__Why are we still here...just to suffer?__***', ''
            ]
        await ctx.send(choice(responses))

def setup(bot: Bot):
    bot.add_cog(embed(bot))
