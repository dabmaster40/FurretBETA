import praw

from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class embed(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Cat', description = 'Sends a cat from r/catpictures')
    async def stats(self, ctx: SlashContext):
        await ctx.send("One second...")
        reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                            client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                            user_agent='script by dabmaster_40')

        submission = reddit.subreddit("catpictures").random()
        await ctx.send(submission.url)

def setup(bot: Bot):
    bot.add_cog(embed(bot))
