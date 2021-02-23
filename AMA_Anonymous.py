import discord, datetime, time, random
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '-', intents = intents)

ama_channel_id = 810362990838415380 #ama ask questions channel
guild_id = 613512375798333450
gaucho_id = 761355746163163138

@client.event
async def on_ready():
    print('Bot is ready')

user_list = []
generated_user = []

# Command to post within the server
######################################################################################################################################################
@client.command(aliases=['whine','r','complaint'])
async def rant(ctx,*,rant):
    k = 0
    if ctx.author not in user_list:
        user = random.randint(0,9999)
        user_list.append(ctx.author)
        generated_user.append(f'User{user}')
        print(f'User: {ctx.author} said: {rant}')
        await ctx.message.delete()
        await ctx.send(f'User{user}: {rant}')
    elif ctx.author in user_list:
        for i in user_list:
            if i == ctx.author:
                print(f'User: {ctx.author} said: {rant}')
                await ctx.message.delete()
                await ctx.send(f'{generated_user[k]}: {rant}')
            k = k + 1

# Direct Message to post in the server
######################################################################################################################################################
@client.listen('on_message')
async def on_message(message):
    guild = client.get_guild(guild_id)
    user_id = message.author.id
    usable_member = guild.get_member(user_id)

    gaucho_role = guild.get_role(gaucho_id)
    usable_member_roles = usable_member.roles

    k = 0

    if gaucho_role in usable_member_roles:
        if message.channel != client.get_channel(ama_channel_id):
            if message.author != client.user:
                if message.author not in user_list:
                    user = random.randint(0,9999)
                    user_list.append(message.author)
                    generated_user.append(f'User{user}')
                    rant2 = str(message.content)
                    channel = client.get_channel(ama_channel_id)
                    print(f'User: {message.author} said: {rant2}')
                    await channel.send(content = f'User{user}: {rant2}')
                elif message.author in user_list:
                    for i in user_list:
                        if i == message.author:
                            rant2 = str(message.content)
                            channel = client.get_channel(ama_channel_id)
                            print(f'User: {message.author} said: {rant2}')
                            await channel.send(content = f'{generated_user[k]}: {rant2}')
                        k = k + 1
                    k = 0 

# Command to view the amount of running time
######################################################################################################################################################
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