import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command()
async def Toplama(ctx, sayi_1, sayi_2):
    await ctx.send(int(sayi_1) + int(sayi_2))

@bot.command()
async def carpma(ctx, sayi_1, sayi_2):
    await ctx.send(int(sayi_1) * int(sayi_2))

@bot.command()
async def bolme(ctx, sayi_1, sayi_2):
    await ctx.send(int(sayi_1) / int(sayi_2))

@bot.command()
async def cikarma(ctx, sayi_1, sayi_2):
    await ctx.send(int(sayi_1) - int(sayi_2))

@bot.command()
async def Yardim(ctx):
    await ctx.send("komutlar: /hello,/heh int,/Toplama int int,/cikarma int int,/carpma int int,/bolme int int,/joined @member")


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


bot.run("Token")