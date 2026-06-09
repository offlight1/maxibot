import os
from discord.ext import commands
import discord
import random

token = 'add yours here'
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents = intents)

commands_list = ['!info', '!rps + your choice', '!poll + your question', '!clear + amount of messages you want cleared.']

@bot.event
async def on_ready():
    channel = bot.get_channel(1513658673996632356)

    if channel:
        await channel.send("Maxibot online. Type !info to see commands.")

@bot.event
async def on_member_join(member: discord.Member):
    await member.send(f"Welcome to {member.guild.name}, {member.mention}!")

@bot.command(name="serverinfo")
# add server information function here
async def show_server_info(ctx):
    guild_voice = ctx.guild.voice_channels
    guild_chat = ctx.guild.text_channels
    creation_date = ctx.guild.created_at

    await ctx.send(f"Guild Name: \n {ctx.guild.name}")
    await ctx.send("----------------------")

    await ctx.send(f"Created: \n {creation_date}")

    await ctx.send("----------------------")
    
    await ctx.send('Text Channels:')
    for txt in guild_chat:
        await ctx.send(txt)

    await ctx.send('----------------------')

    if guild_voice != None:
        await ctx.send("Voice Channels:")
        for vc in guild_voice:
            await ctx.send(vc)

    else:
        await ctx.send(f"No Voice Channels in {ctx.guild.name}")




@bot.command(name="info")
async def show_info(ctx):
    await ctx.send("Available Commands:")
    for cmd in commands_list:
        await ctx.send(cmd)

@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear_chat(ctx, amount: int):
    if amount < 1:
        await ctx.send("Choose an amount higher than 0.")
        return

    deleted = await ctx.channel.purge(limit = amount + 1)

    await ctx.send(f"Deleted {len(deleted) - 1} messages")

@clear_chat.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command!")


@bot.command(name="poll")
async def poll(ctx, *, question: str):
    embed = discord.Embed(
        title = "Community Poll",
        description = question,
        color = discord.Color.blue())

    embed.set_footer(text=f"Poll started by {ctx.author.display_name}")\

    poll_message = await ctx.send(embed=embed)
    
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

@bot.command(name="rps")
async def play_rps(ctx, user_choice: str):
    
    bot_choice = random.choice(["rock", 'paper', 'scissors'])

    decision_dict = {
    "rock" : 'scissors',
    "paper" : 'rock',
    "scissors" : 'paper',
    }


    if user_choice.lower() == bot_choice:
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("We tied!")

    elif decision_dict[user_choice] == bot_choice:
        await ctx.send(f'I chose {bot_choice}')
        await ctx.send("You win!")

    else:
        await ctx.send(f"I chose {bot_choice}")
        await ctx.send("I win!")

bot.run(token)

