from redbot.core import commands, checks, Config
from redbot.core.utils.predicates import ReactionPredicate, MessagePredicate
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu
import contextlib
import discord

"""thanks to Jintaku, taken his original code found here https://github.com/Jintaku/Jintaku-Cogs-V3"""

BaseCog = getattr(commands, "Cog", object)

class Rant(BaseCog):

    def __init__(self):
        self.config = Config.get_conf(self, identifier=665235)
        default_guild = {"rant_room": ""}
        self.config.register_guild(**default_guild)

    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def rantset(self, ctx, *, channel: discord.TextChannel):
        """Set a rant room"""

        rooms = await self.config.guild(ctx.guild).rant_rooms()

        if channel is None:
            return await ctx.send("No channel mentioned.")

        await self.config.guild(ctx.guild).rant_rooms.set(channel.id)
        await ctx.send("The room has been set.")

    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def rantunset(self, ctx):
        """Unset a rant room"""

        rooms = await self.config.guild(ctx.guild).rant_rooms()

        await self.config.guild(ctx.guild).rant_rooms.set("")
        await ctx.send("The room has been unset.")

    @commands.command()
    async def rant(self, ctx, *, rant):
        """Confess your dirty sins

        It'll ask you which guild to rant in if you have more than one with a rant
        """

        async def select_guild(ctx: commands.Context, pages: list, controls: dict, message: discord.Message, page: int, timeout: float, emoji: str):
            # Clean up
            with contextlib.suppress(discord.NotFound):
                await message.delete()
            # Send it off to this function so it sends to initiate search after selecting subdomain
            await self.selected_guild(ctx, user_guilds, rant, page)
            return None

        if bool(ctx.guild):
            await ctx.send("You should do this in DMs!")
            try :
                await ctx.message.delete()
            except:
                pass
            return

        all_guilds = ctx.bot.guilds
        user_guilds = []
        for guild in all_guilds:
            if guild.get_member(ctx.message.author.id):
                room = await self.config.guild(guild).rant_rooms()
                if room is not None:
                    user_guilds.append(guild)

        if len(user_guilds) == 0:
            await ctx.author.send("No server with a rant room, ask your server owners to set it up!")
        if len(user_guilds) == 1:
            await self.send_rant(ctx, user_guilds[0], rant)
        else:
            SELECT_DOMAIN = {"\N{WHITE HEAVY CHECK MARK}": select_guild}

            # Create dict for controls used by menu
            SELECT_CONTROLS = {}
            SELECT_CONTROLS.update(DEFAULT_CONTROLS)
            SELECT_CONTROLS.update(SELECT_DOMAIN)

            embeds = []
            for guild in user_guilds:
                embed = discord.Embed()
                embed.title = "Where do you want to rant?"
                embed.description = guild.name
                embeds.append(embed)

            await menu(ctx, pages=embeds, controls=SELECT_CONTROLS, message=None, page=0, timeout=20)

    async def selected_guild(self, ctx, user_guilds, rant, page):

        rant_guild = user_guilds[page]
        await self.send_rant(ctx, rant_guild, rant)

    async def send_rant(self, ctx, rant_guild, rant):

        rooms = await self.config.guild(rant_guild).rant_rooms()

        for channel in rant_guild.text_channels:
            if rooms == channel.id:
                rant_room = channel

        if not rant_room:
            return await ctx.author.send("The rant room does not appear to exist.")

        try:
            
            embed=discord.Embed(color=0xff0000)
            embed.add_field(name="Rant", value=rant, inline=False)
            await ctx.bot.send_filtered(destination=rant_room, embed=embed)

        except discord.errors.Forbidden:
            return await ctx.author.send("I don't have permission to send messages to this room or something went wrong.")
            

        await ctx.author.send("Your rant has been sent.")
