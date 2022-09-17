from discord import Embed
from discord.ext import commands
from authlib.jose import jwt
import os


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Functions
    @staticmethod
    def generate_token(user, operation, **kwargs):
        header = {"alg": "HS256"}
        key = os.getenv("TOKEN")
        payload = {"id": user.id, "operation": operation}
        payload.update(**kwargs)
        return jwt.encode(header=header, key=key, payload=payload).decode("utf-8")

    # Commands
    @commands.command()
    async def config(self, ctx):
        """Config for booking"""
        await ctx.send(f"Please check your DM 📬.")
        user = ctx.message.author
        token = self.generate_token(user, "CONFIG")
        # link = "https://Discord-Bot.lgf2111.repl.co/config/" + token
        link = "http://0.0.0.0:8080/config/" + token
        embed = Embed(description=f"Fill in your login credentials [here]({link})")
        await user.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Config(bot))
