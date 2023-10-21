import discord
import time
from discord.ext import commands
from discord.commands import slash_command
from function import string_to_bf
from typing import Optional
import brainfuck
import sys
import io
from discord.commands import option

MODE = [
  "encode",
  "decode"
]
class brainfuk(commands.Cog,name='brainfuk'):

  def __init__(self,bot):
    self.bot = bot
  async def command_searcher(self: discord.AutocompleteContext):
    return [
      mode for mode in MODE
    ]

  async def get_commands(ctx: discord.AutocompleteContext):
    return [mode for mode in MODE if mode.startswith(ctx.value.lower())]   

  @slash_command(name='brainfuck',description='brainfuck is an esoteric programming language. This command converts your message to that code.')
  @option("mode", description="Pick a mode", autocomplete=get_commands)
  async def brainfuck(self,ctx,
                      message:str,
                      mode:str,
                      ephemeral:Optional[bool]=False):
    
    if mode == 'encode':      
      o = string_to_bf(message,False)
      embed=discord.Embed(title='Brainfuck',description=f"```bf\n{o}\n//{message}\n```\nFormat : **Brainfuck**\nMode : **Encode**")
      await ctx.respond(embed=embed,ephemeral=ephemeral)
    
    elif mode == 'decode':
      brainfuck_code = message
      output_buffer = io.StringIO()
      sys.stdout = output_buffer
      brainfuck.evaluate(brainfuck_code)
      output = output_buffer.getvalue()
      sys.stdout = sys.__stdout__
      embed=discord.Embed(title='Brainfuck',description=f"Result: `{output}`\nFormat : **Brainfuck**\nMode : **Decode**")
      await ctx.respond(embed=embed,ephemeral=ephemeral)
      



def setup(bot):
	bot.add_cog(brainfuk(bot))
