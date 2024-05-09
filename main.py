import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, *content):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("MTIzMzA4MTY3ODA5Njc2NTAzOQ.GG_ham.WEzuqbV0bNa_PFsShq5YgWAyrs5qbUO5oSvw-w")