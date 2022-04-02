import aiohttp
import asyncio
import discord
from redbot.core import commands

"""
Facts:
- Dog fact | https://some-random-api.ml/facts/dog
- Cat fact | https://some-random-api.ml/facts/cat
- Panda fact | https://some-random-api.ml/facts/panda
- Fox fact | https://some-random-api.ml/facts/fox
- Bird fact | https://some-random-api.ml/facts/bird
- Koala fact | https://some-random-api.ml/facts/koala
- Kangaroo fact | https://some-random-api.ml/facts/kangaroo
- Racoon fact | https://some-random-api.ml/facts/racoon
- Elephant fact | https://some-random-api.ml/facts/elephant
- Giraffe fact | https://some-random-api.ml/facts/giraffe
- Whale fact | https://some-random-api.ml/facts/whale

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

    def __init__(self, bot):
        self.bot = bot

    async def embed_facts(
        self,
        ctx: commands.Context,
        name: str,
        fact: str,
        source: str,
    ):
        embed = await self._embed(
            color=await ctx.embed_colour(),
            title=name,
            description=_("{fact}").format(fact=data["fact"][fact_arg]),
            footer=_("Requested by {req} • From {source}").format(
                req=ctx.author.display_name, source=source
            ),
        )
        return embed

    @commands.command()
    async def dogfact(self, ctx: commands.Context) -> None:
        """Gets a random cat fact."""
        try:
            async with self.__session.get(self.__url) as response:
                fact = (await response.json())["fact"]
                await ctx.send(fact)
                await self.embed_facts(
                    ctx,
                    name=_("Dog Fact"),
                    source="some-random-api.ml",
                    facts_url="https://some-random-api.ml/facts/dog",
                    facts_arg="fact"
                )
        except aiohttp.ClientError:
            log.warning("API call failed; unable to get dog fact")
            await ctx.send("I was unable to get a dog fact.")