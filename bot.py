import discord
from discord.ext import commands
import random

# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Truth and Dare questions
truths = [
    "What is your biggest fear?",
    "What is the most embarrassing thing you have done?",
    "Have you ever lied to a friend? What was it about?",
    "What is your guilty pleasure?",
    "Who was your first crush?",
]

dares = [
    "Do 10 pushups.",
    "Sing a song loudly.",
    "Post an embarrassing photo on social media.",
    "Dance with no music for 1 minute.",
    "Talk in an accent for the next 3 rounds.",
]

# Bot events and commands
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='truth')
async def truth(ctx):
    truth_question = random.choice(truths)
    await ctx.send(truth_question)

@bot.command(name='dare')
async def dare(ctx):
    dare_question = random.choice(dares)
    await ctx.send(dare_question)

@bot.command(name='truthordare')
async def truth_or_dare(ctx):
    await ctx.send("Type 'truth' or 'dare' to receive a challenge!")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['truth', 'dare']
    try:
        msg = await bot.wait_for('message', check=check, timeout=30)
        if msg.content.lower() == 'truth':
            await truth(ctx)
        elif msg.content.lower() == 'dare':
            await dare(ctx)
    except asyncio.TimeoutError: # type: ignore
        await ctx.send("You took too long to respond! Please try again.")

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Please try again.")
    else:
        await ctx.send("An error occurred. Please try again later.")
        print(error)

# Run the bot with the token
bot.run('YOUR_BOT_TOKEN')
