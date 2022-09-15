from discord.ext import commands
from replit import db

# from main import session
# from models import Guild


class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guilds, id = db['guilds'], str(guild.id)
        guilds[id] = {
            'prefix': '.'
        }
        db['guilds'] = guilds
        # guild_ = Guild(id=guild.id)
        # session.add(guild_)
        # session.commit()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guilds, id = db['guilds'], str(guild.id)
        del guilds[id]
        db['guilds'] = guilds
        # guild_ = session.query(Guild).filter_by(id=guild.id).first()
        # session.delete(guild_)
        # session.commit()

    # Commands
    @commands.command()
    async def chpf(self, ctx, new_pfx):
        """Change prefix"""
        id = str(ctx.guild.id)
        guild = db['guilds'][id]
        old_pfx = guild['prefix']
        guild['prefix'] = new_pfx
        db['guilds'][id] = guild
        await ctx.send(f"Prefix changed from {old_pfx} to {new_pfx}")
        # guild = session.query(Guild).filter_by(id=ctx.guild.id).first()
        # temp = guild.prefix
        # guild.prefix = prefix
        # session.commit()
        # await ctx.send(f"Prefix changed from {temp} to {prefix}")

    # @tree.command()
    # async def slash_change_prefix(self, ctx: Interaction, prefix: str):
    #     """Change prefix"""
    #     guild = session.query(Guild).filter_by(id=ctx.guild.id).first()
    #     temp = guild.prefix
    #     guild.prefix = prefix
    #     session.commit()
    #     print(f"Prefix changed from {temp} to {prefix}!")


async def setup(bot):
    await bot.add_cog(Prefix(bot))
