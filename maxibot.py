import os
from discord.ext import commands
import discord
import random

token = 'enter yours here'
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
    
    #var setup
    bot_choice = random.randint(1, 3)
    rock = 1
    paper = 2
    scissors = 3


    #turn user option into an int
    if user_choice.lower() == 'rock':
        user_choice = rock

    elif user_choice.lower() == 'paper':
        user_choice = paper

    elif user_choice.lower() == 'scissors':
        user_choice = scissors

    
    #bot logic 
    if bot_choice == rock and user_choice == rock:
        await ctx.send("I chose rock.")
        await ctx.send("We tied!")

    elif bot_choice == rock and user_choice == paper:
        await ctx.send("I chose rock.")
        await ctx.send("You Win!")

    elif bot_choice == rock and user_choice == scissors:
        await ctx.send("I chose rock.")
        await ctx.send("I win!")

    elif bot_choice == paper and user_choice == rock:
        await ctx.send("I chose paper.")
        await ctx.send("I win!")

    elif bot_choice == paper and user_choice == paper:
        await ctx.send("I chose paper.")
        await ctx.send("We tied!")

    elif bot_choice == paper and user_choice == scissors:
        await ctx.send("I chose paper.")
        await ctx.send("You Win!")

    elif bot_choice == scissors and user_choice == rock:
        await ctx.send("I chose scissors.")
        await ctx.send("You Win!")

    elif bot_choice == scissors and user_choice == paper:
        await ctx.send("I chose scissors.")
        await ctx.send("I Win!")

    elif bot_choice == scissors and user_choice ==  scissors:
        await ctx.send("I chose scissors.")
        await ctx.send("We tied!")

bot.run(token)

