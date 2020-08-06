# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
from discord.ext.commands.errors import CommandInvokeError, MissingRequiredArgument
from helpers.search import gen_embeds, validate, get_emoji


class Emojilist(commands.Cog):
    """Lists emoji"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="search")
    async def esearch(self, ctx, name, page: int = 1):
        page = page - 1
        if not validate(name):
            await ctx.channel.send("Emoji names must be between 2 and 32 characters", delete_after=15)
            return

        embeds = gen_embeds(self.bot.emojis, name)
        if page + 1 > len(embeds):
            insert = f'is only {len(embeds)} page' if len(embeds) == 1 else f'are only {len(embeds)} pages'
            text = f"There {insert} for this result"
            await ctx.channel.send(text, embed=embeds[len(embeds)-1])
            return
        await ctx.channel.send(embed=embeds[page])

    @commands.command(name="emoji")
    async def eemoji(self, ctx, *namesOrIDs):
        message = ""
        for name in namesOrIDs:
            message += " " + get_emoji(self.bot.emojis, name)
        await ctx.channel.send(message)

    @esearch.error
    async def search_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.channel.send("Usage: `%search <name> [page]`", delete_after=15)
        print(error)

    @eemoji.error
    async def emoji_error(self, ctx, error):
        if isinstance(error, CommandInvokeError):
            await ctx.channel.send("You must specifiy a valid emoi name or ID. Usage: `%emoji <name or ID>`", delete_after=15)
        print(error)


def setup(bot):
    bot.add_cog(Emojilist(bot))
