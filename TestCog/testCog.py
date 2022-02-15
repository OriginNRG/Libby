from redbot.core import commands

class TestCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testcog(self, ctx):
        await ctx.send("Just a test.")