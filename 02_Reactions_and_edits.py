import discord

client = discord.Client()

@client.event
async def on_ready():
    print('online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'cool':
        await  message.add_reaction('\U0001F60E')

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message. \n'
        f'before: {before.content} \n '
        f'after: {after.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(
        f'{user} reacted with {reaction.emoji}'
    )

client.run('OTE5MTMxODk4Njc1MDkzNTU2.YbRWSQ.JXBTWQpdWeuBimxUdgbgzPMX4us')