import wavelink
from discord.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='>?')

class music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
                                            host='0.0.0.0',
                                            port=2333,
                                            password='YOUR_LAVALINK_PASSWORD')

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack):
        """Play a song with the given search query.
        If not connected, connect to our voice channel.
        """
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.queue.put_wait(search)
            await vc.play(search)
            await ctx.send(f'Added `{search.title}` to the queue...', delete_after=10)

        else:
            await vc.queue.put_wait(search)
            await ctx.send(f'Added `{search.title}` to the queue...', delete_after=10)

    @commands.command()
    async def queue(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client

        if not vc:
            return await ctx.send('No queue as we are not connected', delete_after=5)

        await ctx.send(vc.queue)


def setup(bot: Bot):
    bot.add_cog(music(bot))