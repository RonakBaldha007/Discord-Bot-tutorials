import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.command()
async def help(ctx):

    embed = discord.Embed(
        title="bot command",
        description="Welcome to the help section. Here are all commands for this game",
        color= discord.Colour.green()
    )

    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/67002427?v=4")

    embed.add_field(
        name='!help',
        value='List all of the command',
        inline=False
    )
    embed.add_field(
        name='!punch',
        value='This commands punches another players',
        inline=False
    )
    embed.add_field(
        name='!roundhouse_kick',
        value='This commands roundhouse kick another players',
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Ronak ricky
    """
    await ctx.send(f'Double Punched {arg1} and {arg2}')

@bot.command()
async def punch(ctx, arg):
    """
    This commands punches another players
    """
    await ctx.send(f'Punched {arg}')

@bot.command()
async def roundhouse_kick(ctx, *args):
    """
    !roundhouse_kick Ronak ricky justin kohli
    """

    everyone = ', '.join(args)
    await ctx.send(f"roundhouse kick {everyone}")

@bot.command()
async def info(ctx):
    """
    ctx - context (Information about how the command executed)

    !info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

bot.run('OTE5MTMxODk4Njc1MDkzNTU2.YbRWSQ.cPKbZiR34Wzg-4KpoqMeKhofhJE')