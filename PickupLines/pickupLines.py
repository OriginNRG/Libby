from random import choice
from typing import List
from pathlib import Path
from redbot.core import commands

flirts = open(Path(__file__).parent / "lines.txt").read().splitlines()

class PickupLines(commands.Cog):

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