from discord.ext import commands
from bot import session
from models import Guild


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guild_ = Guild(id=guild.id)
        session.add(guild_)
        session.commit()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guild_ = session.query(Guild).filter_by(id=guild.id).first()
        session.delete(guild_)
        session.commit()

    # Commands
    @commands.command()
    async def change_prefix(self, ctx, prefix):
        """Change prefix"""
        guild = session.query(Guild).filter_by(id=ctx.guild.id).first()
        guild.prefix = prefix
        session.commit()


async def setup(bot):
    await bot.add_cog(Prefix(bot))
