import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bet = commands.Bot(command_prefix = '&', intents = intents)

@bet.event
async def on_ready():
    print(">> Bot is online")

@bet.event
async def on_member_join(member):
    channel_in = bet.get_channel(994953664009601147)
    await channel_in.send(f"{member} 你過來一下")

@bet.event
async def on_member_remove(member):
    channel_out = bet.get_channels(994958557042712617)
    await channel_out.send(f"滾啦 {member}")

bet.run("OTk0OTQ2MTIyNjM4NDQyNDk2.GIIVxq.VrNkbCFp3DJ8A-XShNu543OWzOjnSGxpV6Ol2I")