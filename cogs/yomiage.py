import discord
import httpx
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.http = httpx.AsyncClient()

async def setup(bot: commands.Bot):
    await bot.add_cog(ExampleCog(bot))