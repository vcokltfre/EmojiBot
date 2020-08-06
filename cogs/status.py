# -*- coding: utf-8 -*-

from discord.ext import commands
import discord


class Status(commands.Cog):
    """Update the status with the current number of loaded emojis"""

    def __init__(self, bot):
        self.bot = bot

    async def update(self):
        await self.bot.change_presence(activity=discord.Game(name=f"with {len(self.bot.emojis)} emojis | %help"))

    @commands.Cog.listener()
    async def on_ready(self):
        await self.update()
        print(f"Client connected as {self.bot.user} ({self.bot.user.id}) with {len(self.bot.guilds)} guilds and {len(self.bot.emojis)} emojis")

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        await self.update()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        await self.update()
    
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild: discord.Guild, before, after):
        await self.update()

def setup(bot):
    bot.add_cog(Status(bot))
