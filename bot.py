import discord
import json
import os
import asyncio
from discord.ext import commands

from models import Session, Guild

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


@bot.command()
async def load(ctx, extension):
    """Load cog"""
    await bot.load_extension(f"cogs.{extension}")


@bot.command()
async def unload(ctx, extension):
    """Unload cog"""
    await bot.unload_extension(f"cogs.{extension}")


@bot.command()
async def reload(ctx, extension):
    """Reload cog"""
    await bot.load_extension(f"cogs.{extension}")
    await bot.unload_extension(f"cogs.{extension}")


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.environ.get("SECERET_KEY"))


if __name__ == "__main__":
    asyncio.run(main())
