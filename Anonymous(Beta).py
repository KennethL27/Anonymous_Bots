"""
Created on Fri Oct 30 14:13:48 2020

@author: Kenneth Lara
"""
import discord, datetime, time
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '-', intents = intents)

rant_channel_id = 771845526903586847 #this variable changes where the DM will go to
guild_id = 730489460113801256
gaucho_id = 759317762769420310

@client.event
async def on_ready():
    print('Bot is ready')

# Anonymous command
######################################
@client.command(aliases=['whine','r','complaint'])
async def rant(ctx,*,rant):
    print(f'User: {ctx.author} said: {rant}')
    await ctx.channel.purge(limit=1)
    await ctx.send(rant)

# Direct Message to post anonymous to the channel in line 16
######################################
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
    '''
    if message.channel == client.get_channel(rant_channel_id):
        if message.author != client.user:
            if message.content.startswith('-r'):
                await message.channel.purge(limit=1)
                await client.get_channel(rant_channel_id).send(str(message.content))
                print(f'User: {message.author} said: {message.content}')
            if message.content.startswith('-whine'):
                await message.channel.purge(limit=1)
                await client.get_channel(rant_channel_id).send(str(message.content))
                print(f'User: {message.author} said: {message.content}')
            if message.content.startswith('-rant'):
                await message.channel.purge(limit=1)
                await client.get_channel(rant_channel_id).send(str(message.content))
                print(f'User: {message.author} said: {message.content}')
            if message.content.startswith('-complain'):
                await message.channel.purge(limit=1)
                await client.get_channel(rant_channel_id).send(str(message.content))
                print(f'User: {message.author} said: {message.content}')
            '''    

# Uptime Command
######################################
@client.command()
async def uptime(ctx):
    await ctx.channel.purge(limit = 1)
    time_seconds = time.perf_counter()
    time_days = time_seconds //(86400)
    time_seconds = time_seconds % 86400
    time_hours = time_seconds // 3600
    time_seconds %= 3600
    time_minutes =  time_seconds // 60
    time_seconds %= 60
    time_seconds = time_seconds
    message = await ctx.send(f'**UPTIME**: Days: {int(time_days)}, Hours: {int(time_hours)}, Minutes: {int(time_minutes)}, Seconds: {round(time_seconds,2)}')
    await message.delete(delay = 5)

client.run('TOKEN')