import os

import discord
import dotenv
import httpx
from discord.ext import commands

dotenv.load_dotenv()

class YomiageCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.http = httpx.AsyncClient()
        self.channelId: int = None

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.channel.id != channelId:
            return
        text = message.clean_content
        source = discord.FFmpegPCMAudio("https://deprecatedapis.tts.quest/v2/voicevox/audio/?text={text}&key={os.getenv('vvapikey')}"
        message.guild.voice_client.play(source)

    @commands.command()
    async def join(self, ctx: commands.Context):
        if not ctx.author.voice:
            await ctx.message.add_reaction("❌")
        await ctx.author.voice.channel.connect()
        self.channelId = ctx.author.voice.channel.id
        await ctx.message.add_reaction("⭕️")

async def setup(bot: commands.Bot):
    await bot.add_cog(YomiageCog(bot))