import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online and ready to roll')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        await  message.channel.send('Hey')

client.run('OTE5MTMxODk4Njc1MDkzNTU2.YbRWSQ.JXBTWQpdWeuBimxUdgbgzPMX4us')