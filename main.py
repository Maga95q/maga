import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
#бот приветствуется 
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    
#отпрабляет столько раз heh сколько раз захочет игрок
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#повторяет сообшение множество раз
@bot.command()
async def repeat(ctx, times: int, *content):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
#говорит когда в группу присоединяется человек
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
#ссоединяет два числа 
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


bot.run("MTIzMzA4MTY3ODA5Njc2NTAzOQ.GG_ham.WEzuqbV0bNa_PFsShq5YgWAyrs5qbUO5oSvw-w")







