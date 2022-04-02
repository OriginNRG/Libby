from .somerandomapi import SomeRandomAPI


def setup(bot):
    n = SomeRandomAPI()
    bot.add_cog(n)
