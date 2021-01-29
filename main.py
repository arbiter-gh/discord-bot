import discord
from discord.ext import commands
from bot_token import bot_token
import time
import asyncio

messages = joined = 0

valid_channels = ['commands']
valid_users = ['ArbitEr#0507']
greetings = ["Hi", "hi", "Hello", "hello", "Hii", "hii"]

client = discord.Client()

@client.event
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt","a") as f:
                f.write(f"Time : {int(time.time())}, Messages : {messages}, Joined : {joined}\n")

            messages = 0
            joined = 0
            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print("Arbitrator BOT is ready.")

@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f'Hello {member.mention} , Welcome to this Server')

@client.event
async def on_message(message):
    global messages
    messages += 1
    id = client.get_guild(803147327195971614)

    if message.author == client.user:
        return
    if str(message.channel) in valid_channels and str(message.author) in valid_users:

        if message.content in greetings:
            await message.channel.send(f'Hello {message.author.mention}')
           
        elif message.content == ".users":
            await message.channel.send(f"There are total **{id.member_count}** member(s). Online Users {users}")
        
    
    else:
        print(f"{message.author} tried to send command {message.content} in channel {message.channel}")


client.loop.create_task(update_stats())
client.run(bot_token)