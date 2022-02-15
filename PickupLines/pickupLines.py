from random import choice
from typing import List
from redbot.core import commands

flirts = open('file.txt').read().splitlines()

class PickupLines(commands.Cog):

	_author = ["Origin"]
    _version = "0.0.1"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flirt(self, ctx: commands.Context, user: discord.Member = None) -> None:
        msg = " "
        if user:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await ctx.send(ctx.message.author.mention + msg + choice(flirts))
            else:
                await ctx.send(user.mention + msg + choice(flirts))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(flirts))