import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_message(message):
    if message.content.lower() == "hi ctfu bot":
        await message.channel.send("Hello! :wave:")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided!"):
        await user.kick(reason=reason)
        kick = discord.Embed(title=f"Kicked {member}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.channel.send(embed=kick)
        dm_kick = discord.Embed(title=f"You were kicked!", description = f"Reason: {reason}\nBy: {ctx.message.author}\nServer: {ctx.guild.name}")
        await member.send(embed=kick)

bot.run(TOKEN)
