import discord
from discord.commands import slash_command
from discord.ext import commands
import time


class ping(commands.Cog,name='ping'):

  def __init__(self,bot):
    self.bot = bot
  

  @slash_command()
  async def hello(self, ctx):
    await ctx.send('Hello!')

  @slash_command()
  async def ping(self, ctx):
    before = time.monotonic()
    message = await ctx.respond("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit_original_response(content=f"Ping:  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')


def setup(bot):
	bot.add_cog(ping(bot))