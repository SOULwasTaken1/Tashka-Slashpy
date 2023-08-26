import discord
import time
from discord.ext import commands
from discord.commands import slash_command
from function import string_to_bf
from typing import Optional

class brainfuk(commands.Cog,name='brainfuk'):

  def __init__(self,bot):
    self.bot = bot
   

  @slash_command(name='brainfuck',description='brainfuck is an esoteric programming language. This command converts your message to that code.')
  async def brainfuck(self,ctx,message:str,ephemeral:Optional[bool]=False):

    o = string_to_bf(message,False)
    await ctx.respond(f"```bf\n{o}\n//{message}\n```",ephemeral=ephemeral)



def setup(bot):
	bot.add_cog(brainfuk(bot))