from .pickupLines import PickupLines


def setup(bot):
    bot.add_cog(PickupLines(bot))