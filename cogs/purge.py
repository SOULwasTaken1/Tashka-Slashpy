import discord
from discord.ext import commands
from discord.commands import slash_command
from typing import Optional
from discord import TextChannel

class purge(commands.Cog,name='purge'):

  def __init__(self,bot):
    self.bot = bot
  
  @slash_command(name="purge", description="Mass deletes messages from a channel")
  @commands.has_permissions(administrator=True) 
  async def purge(self, ctx, amount:Optional[int] = 11): 
    amount += 1
    if amount > 10000: 
      return await ctx.respond("I am not able to delete that many messages")
    else:
      await ctx.respond("Deleting messages...",delete_after=0)
      channel_id = ctx.channel.id
      tempAmount = amount 
      tempAmount -= 1
      amountAsString = str(tempAmount) 
      await ctx.channel.purge(limit=amount)
      embed=discord.Embed(title="Purge", description=f"Purged **{amountAsString}** Messages from <#{channel_id}>", color=0x070303)
      await ctx.send(embed=embed,delete_after=5)

  @slash_command(name='nuke',description='Nukes a channel')
  @commands.has_permissions(administrator=True) 
  async def nuke(self, ctx, channel:TextChannel):
    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if nuke_channel is not None:
      new_channel = await nuke_channel.clone(reason="Has been Nuked!")
      await nuke_channel.delete()
      await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
      await ctx.send("Nuked the Channel sucessfully!")

    else:
      return await ctx.respond(f"No channel named {channel.name} was found!")



def setup(bot):
	bot.add_cog(purge(bot))