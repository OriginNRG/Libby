import json
import aiohttp
import asyncio
import discord
from redbot.core import checks, Config, commands
from redbot.core.utils.chat_formatting import bold, box, inline
from random import choice
from typing import Optional, Union

"""

Images:
- Dog Image | https://some-random-api.ml/img/dog
- Cat Image | https://some-random-api.ml/img/cat
- Panda Image | https://some-random-api.ml/img/panda
- Red panda Image | https://some-random-api.ml/img/red_panda
- Fox Image | https://some-random-api.ml/img/fox
- Birb(bird) Image | https://some-random-api.ml/img/birb
- Koala Image | https://some-random-api.ml/img/koala
- Kangaroo Image | https://some-random-api.ml/img/kangaroo
- Racoon Image | https://some-random-api.ml/img/racoon
- Whale Image | https://some-random-api.ml/img/whale
- Pikachu Image | https://some-random-api.ml/img/pikachu 

Others:
- Meme | https://some-random-api.ml/meme
- Joke | https://some-random-api.ml/joke
"""

class SomeRandomAPI(commands.Cog):
    def __init__(self, bot, *args, **kwargs) -> None:

        self.bot = bot

        self.__dog_fact: str = "https://some-random-api.ml/facts/dog"
        self.__cat_fact: str = "https://some-random-api.ml/facts/cat"
        self.__panda_fact: str = "https://some-random-api.ml/facts/panda"
        self.__fox_fact: str = "https://some-random-api.ml/facts/fox"
        self.__bird_fact: str = "https://some-random-api.ml/facts/bird"
        self.__koala_fact: str = "https://some-random-api.ml/facts/koala"
        self.__kangaroo_fact: str = "https://some-random-api.ml/facts/kangaroo"
        self.__racoon_fact: str = "https://some-random-api.ml/facts/racoon"
        self.__elephant_fact: str = "https://some-random-api.ml/facts/elephant"
        self.__giraffe_fact: str = "https://some-random-api.ml/facts/giraffe"
        self.__whale_fact: str = "https://some-random-api.ml/facts/whale"

        self.__dog_image: str = "https://some-random-api.ml/img/dog"
        self.__cat_image: str = "https://some-random-api.ml/img/cat"
        self.__panda_image: str = "https://some-random-api.ml/img/panda"
        self.__red_panda_image: str = "https://some-random-api.ml/img/red_panda"
        self.__fox_image: str = "https://some-random-api.ml/img/fox"
        self.__bird_image: str = "https://some-random-api.ml/img/birb"
        self.__koala_image: str = "https://some-random-api.ml/img/koala"
        self.__kangaroo_image: str = "https://some-random-api.ml/img/kangaroo"
        self.__racoon_image: str = "https://some-random-api.ml/img/racoon"
        self.__whale_image: str = "https://some-random-api.ml/img/whale"
        self.__pikachu_image: str = "https://some-random-api.ml/img/pikachu"

        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    async def embed_fact(self,ctx,title: str,description: str):
        author = ctx.author.display_name
        color = await ctx.embed_color()
        e = discord.Embed(color=color, title=title, description=description)
        e.set_footer(text="Requested by: " + author)
        await ctx.send(embed=e)

    @commands.command()
    async def dogfact(self, ctx: commands.Context) -> None:
        """Gets a random dog fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__dog_fact) as response:
                description = (await response.json())["fact"]
                title="Dog Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a dog fact.`")

    @commands.command()
    async def catfact(self, ctx: commands.Context) -> None:
        """Gets a random cat fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__cat_fact) as response:
                description = (await response.json())["fact"]
                title="Cat Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a cat fact.`")
    
    @commands.command()
    async def pandafact(self, ctx: commands.Context) -> None:
        """Gets a random panda fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__panda_fact) as response:
                description = (await response.json())["fact"]
                title="Panda Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a panda fact.`")

    @commands.command()
    async def foxfact(self, ctx: commands.Context) -> None:
        """Gets a random fox fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__fox_fact) as response:
                description = (await response.json())["fact"]
                title="Fox Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a fox fact.`")

    @commands.command()
    async def birdfact(self, ctx: commands.Context) -> None:
        """Gets a random bird fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__bird_fact) as response:
                description = (await response.json())["fact"]
                title="Bird Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a bird fact.`")

    @commands.command()
    async def koalafact(self, ctx: commands.Context) -> None:
        """Gets a random koala fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__koala_fact) as response:
                description = (await response.json())["fact"]
                title="Koala Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a koala fact.`")

    @commands.command()
    async def kangaroofact(self, ctx: commands.Context) -> None:
        """Gets a random kangaroo fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__kangaroo_fact) as response:
                description = (await response.json())["fact"]
                title="Kangaroo Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a kangaroo fact.`")

    @commands.command()
    async def racoonfact(self, ctx: commands.Context) -> None:
        """Gets a random racoon fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__racoon_fact) as response:
                description = (await response.json())["fact"]
                title="Racoon Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a racoon fact.`")

    @commands.command()
    async def elephantfact(self, ctx: commands.Context) -> None:
        """Gets a random elephant fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__elephant_fact) as response:
                description = (await response.json())["fact"]
                title="Elephant Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a elephant fact.`")

    @commands.command()
    async def giraffefact(self, ctx: commands.Context) -> None:
        """Gets a random giraffe fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__giraffe_fact) as response:
                description = (await response.json())["fact"]
                title="Giraffe Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a giraffe fact.`")

    @commands.command()
    async def whalefact(self, ctx: commands.Context) -> None:
        """Gets a random whale fact."""
        await ctx.trigger_typing()
        try:
            async with self.__session.get(self.__whale_fact) as response:
                description = (await response.json())["fact"]
                title="Whale Fact"
                await self.embed_fact(ctx,title,description)
        except aiohttp.ClientError:
            await ctx.send("`I was unable to get a whale fact.`")