import discord, time
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '-', intents = intents)

rant_channel_id = 718972914434572402
guild_id = 613512375798333450
gaucho_id = 761355746163163138

@client.event
async def on_ready():
    print('Bot is ready')

# User Commands
######################################################################################################################################################
@client.command(aliases=['whine','r','complaint'])
async def rant(ctx,*,rant):
    print(f'User: {ctx.author} said: {rant}')
    await ctx.channel.purge(limit=1)
    await ctx.send(rant)

@client.command()
async def uptime(ctx):
    time_seconds = time.perf_counter()
    time_days = time_seconds //(86400)
    time_seconds = time_seconds % 86400
    time_hours = time_seconds // 3600
    time_seconds %= 3600
    time_minutes =  time_seconds // 60
    time_seconds %= 60
    time_seconds = time_seconds
    await ctx.send(f'**UPTIME**: Days: {int(time_days)}, Hours: {int(time_hours)}, Minutes: {int(time_minutes)}, Seconds: {round(time_seconds,2)}')

# DM Feature
######################################################################################################################################################
@client.listen('on_message')
async def on_message(message):
    guild = client.get_guild(guild_id)
    user_id = message.author.id
    usable_member = guild.get_member(user_id)
   
    gaucho_role = guild.get_role(gaucho_id)
    usable_member_roles = usable_member.roles
   
    if gaucho_role in usable_member_roles:
        if message.channel != client.get_channel(rant_channel_id):
            if message.author != client.user:
                rant2 = str(message.content)
                channel = client.get_channel(rant_channel_id)
                print(f'User: {message.author} said: {rant2}')
                await channel.send(content = rant2)

client.run('TOKEN')