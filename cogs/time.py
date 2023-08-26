import discord
from discord.commands import slash_command
from discord.ext import commands
import time as t
from function import time_conv,conv
from discord.commands import option

TENSE = [
  "future",
  "past",
  "present"
]

class time(commands.Cog,name='time'):

  def __init__(self,bot):
    self.bot = bot
  
  async def command_searcher(self: discord.AutocompleteContext):
    return [
      tense for tense in TENSE
    ]

  async def get_commands(ctx: discord.AutocompleteContext):
    return [tense for tense in TENSE if tense.startswith(ctx.value.lower())]

  @slash_command(name="time",description="Generates a Discord timestamp")
  @option("tense", description="Select a tense", autocomplete=get_commands)
  async def time(self, ctx,tense,add):
    
    unixCode = int(t.time())
    pfp = ctx.author.avatar
    add_tu = add.split(' ')
    add_time= int(conv(add_tu))
  
    if tense == 'present':
      embed=discord.Embed(title="Time generator", description=f"Unix Code: **{unixCode}** \nTimestamp: <t:{unixCode}:R>\n**Copy the text Below:** \n `<t:{unixCode}:R>`", color=0x0b0505) 
      embed.set_thumbnail(url=(pfp))
      await ctx.respond(embed=embed)
    if tense == 'future':
      futureTime = unixCode + add_time 
      embed=discord.Embed(title="Time generator", description=f"Unix Code: **{futureTime}** \nTimestamp: <t:{futureTime}:R>\n**Copy the text Below:** \n `<t:{futureTime}:R>`", color=0x0b0505)
      embed.set_thumbnail(url=(pfp)) 
      await ctx.respond(embed=embed)
    if tense == 'past':
      pastTime = unixCode - add_time 
      embed=discord.Embed(title="Time generator", description=f"Unix Code: **{pastTime}** \nTimestamp: <t:{pastTime}:R>\n**Copy the text Below:** \n `<t:{pastTime}:R>`", color=0x0b0505) 
      embed.set_thumbnail(url=(pfp))
      await ctx.respond(embed=embed)


def setup(bot):
	bot.add_cog(time(bot))