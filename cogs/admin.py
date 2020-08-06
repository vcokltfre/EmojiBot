# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import time
import datetime

owners = [297045071457681409]

def getTime():
    return round(time.time())

class Admin(commands.Cog):
    """Administrator utilities"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.start = getTime()

    @commands.command(name="restart", aliases=["emojirestart", "erestart"], hidden=True)
    async def restart(self, ctx):
        if ctx.author.id in owners:
            await self.bot.logout()
        else:
            await ctx.channel.send("You don't have permission to run this command!", delete_after=10)

    @commands.command(name="einfo", hidden=True)
    async def info(self, ctx):
        if not ctx.author.id in owners:
            await ctx.channel.send("You don't have permission to run this command!", delete_after=10)
            return
        embed = discord.Embed(title="EmojiBot Info")
        embed.add_field(name="Uptime", value=f"{datetime.timedelta(seconds=getTime()-self.start)}")
        embed.add_field(name="Guilds", value=f"{len(self.bot.guilds)}")

        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
