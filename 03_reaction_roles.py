import discord

"""

@client.event
async def on_ready():
    print('online')
    
client = discord.Client()

client.run('OTE5MTMxODk4Njc1MDkzNTU2.YbRWSQ.JXBTWQpdWeuBimxUdgbgzPMX4us')

"""


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 919161743010332682

    async def on_ready(self):
        print('ready')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based ona reaction emoji
        """

        if payload.message_id == self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == '🍉':
            role = discord.utils.get(guild.roles, name='melon person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='chocolate lover')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='funky monkey')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        remove a role based ona reaction emoji
        """

        if payload.message_id == self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🍉':
            role = discord.utils.get(guild.roles, name='melon person')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='chocolate lover')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='funky monkey')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('OTE5MTMxODk4Njc1MDkzNTU2.YbRWSQ.cPKbZiR34Wzg-4KpoqMeKhofhJE')
