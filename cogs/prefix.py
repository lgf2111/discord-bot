from discord.ext import commands
from replit import db


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def chpf(self, ctx, new_pfx):
        """Change prefix"""
        id = str(ctx.guild.id)
        guild = db["guilds"][id]
        old_pfx = guild["prefix"]
        guild["prefix"] = new_pfx
        db["guilds"][id] = guild
        await ctx.send(f"Prefix changed from {old_pfx} to {new_pfx}")

    @commands.command()
    async def crpf(self, ctx):
        """Current prefix"""
        id = str(ctx.guild.id)
        guild = db["guilds"][id]
        pfx = guild["prefix"]
        await ctx.send(
            f"Current prefix is {pfx} (You're literally using it right now...LOL)"
        )


async def setup(bot):
    await bot.add_cog(Prefix(bot))
