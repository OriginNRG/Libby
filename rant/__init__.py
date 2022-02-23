from .rant import Rant


def setup(bot):
    n = Rant()
    bot.add_cog(n)
