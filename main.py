is_replit = True
try:
    from replit import db
except ImportError:
    is_replit = False

import discord
import os
import asyncio

# from discord import app_commands
from discord.ext import commands

from models import Session, Guild
from maintain import maintain

session = Session()


def get_prefix(bot, message):
    guild = session.query(Guild).filter_by(id=message.guild.id).first()
    if guild == None:
        guild_ = Guild(id=message.guild.id)
        session.add(guild_)
    return guild.prefix


help_command = commands.DefaultHelpCommand(no_category="Commands")
discord.utils.setup_logging()
bot = commands.Bot(
    intents=discord.Intents.all(), command_prefix=get_prefix, help_command=help_command
)

# intents = discord.Intents.default()
# intents.message_content = True

# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)


@bot.command()
async def load(ctx, extension):
    """Load cog"""
    cog = f"cogs.{extension}"
    await bot.load_extension(cog)


@bot.command()
async def unload(ctx, extension):
    """Unload cog"""
    cog = f"cogs.{extension}"
    await bot.unload_extension(f"cogs.{extension}")


@bot.command()
async def reload(ctx, extension):
    """Reload cog"""
    cog = f"cogs.{extension}"
    await bot.load_extension(f"cogs.{extension}")
    await bot.unload_extension(f"cogs.{extension}")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog = f"cogs.{filename[:-3]}"
            await bot.load_extension(cog)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.environ.get("SECERET_KEY"))


if __name__ == "__main__":
    maintain()
    asyncio.run(main())
