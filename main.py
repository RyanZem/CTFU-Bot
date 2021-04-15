import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_message(ctx):
    if message.content.lower() == "hi ctfu bot":
    await ctx.send("Hello! :wave:")


bot.run(TOKEN)
