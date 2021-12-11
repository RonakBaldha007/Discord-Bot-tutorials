from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Ronak ricky
    """
    await ctx.send(f'Double Punched {arg1} and {arg2}')

@bot.command()
async def punch(ctx, arg):
    """
    !punch
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