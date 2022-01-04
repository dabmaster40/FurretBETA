import praw
from random import choice
from discord import Embed
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

#Playlist==Commands===============================================

class basic(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'Bye', description = 'Says bye')
    async def bye(self, ctx: SlashContext):
        responses = ['finally', 'cya', 'oh ok....']
        await ctx.send(choice(responses))

    @cog_ext.cog_slash(name = 'Cat', description = 'Sends a cat from r/catpictures')
    async def cat(self, ctx: SlashContext):
        await ctx.send("One second...")
        reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                            client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                            user_agent='script by dabmaster_40')

        submission = reddit.subreddit("catpictures").random()
        await ctx.send(submission.url)

    @cog_ext.cog_slash(name = 'Dog', description = 'Sends a dog from r/dogpictures')
    async def dog(self, ctx: SlashContext):
        await ctx.send("One second...")
        reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                            client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                            user_agent='script by dabmaster_40')
        submission = reddit.subreddit("dogpictures").random()
        await ctx.send(submission.url)

    @cog_ext.cog_slash(name = 'Hello', description = 'Says hello')
    async def hello(self, ctx: SlashContext):
        responses = [
            '***grumble*** Why did you wake me up?', 'Hewwo uwu', '***z z z z z***', 'Hello, how are you?', 'Hi', '**...pardon?**', 'Hi! My names furret!', '***__Why are we still here...just to suffer?__***', ''
            ]
        await ctx.send(choice(responses))

    @cog_ext.cog_slash(name = 'Meme', description = 'Sends a meme from r/memes')
    async def meme(self, ctx: SlashContext):
        await ctx.send("One second...")
        reddit = praw.Reddit(client_id='ZFJY9-jVn1-Q67QViinHYA',
                            client_secret='kRvW3fiQk6M1fSO-G7Ylp_u2iTThLg',
                            user_agent='script by dabmaster_40')

        submission = reddit.subreddit("memes").random()
        await ctx.send(submission.url)

    @cog_ext.cog_slash(name = 'Review', description = 'Links the top.gg page for Furret')
    async def review(self, ctx: SlashContext):
        embed = Embed(title='Like Furret?', description= 'Please review Furret here!' + "(https://top.gg/bot/884858660935827467)")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'Support', description = 'Sends a link to Furret\'s Support Server')
    async def support(self, ctx: SlashContext):
        await ctx.send(f"Click below to go to Furret's Support Server!")
        await ctx.send(f"https://discord.gg/8vscBHSNqA")


def setup(bot: Bot):
    bot.add_cog(basic(bot))
