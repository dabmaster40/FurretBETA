import praw

from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class meme(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Meme', description = 'Sends a meme from r/memes')
    async def stats(self, ctx: SlashContext):
        await ctx.send("One second...")
        reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                            client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                            user_agent='script by dabmaster_40')

        submission = reddit.subreddit("memes").random()
        await ctx.send(submission.url)

def setup(bot: Bot):
    bot.add_cog(meme(bot))
