import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_message(ctx):
    if "hi ctfu bot" in message.content.lower():
        await ctx.send("Hello! :wave:")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided!"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)

bot.run(TOKEN)
