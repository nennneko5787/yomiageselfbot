import os

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()

bot = commands.Bot("v#")

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.yomiage")

bot.run(os.getenv("discord")