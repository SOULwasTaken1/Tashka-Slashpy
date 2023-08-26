import discord
from function import BMR
import asyncio
from discord.ext import commands
from discord.commands import slash_command
from Emojies import Rosaria

class bmr(commands.Cog,name='bmr'):

  def __init__(self,bot):
    self.bot = bot
  

  @slash_command(name = 'bmr', description='Calculates your BMR')
  async def bmr(self,ctx):
    pfp = ctx.author.avatar
    await ctx.respond('Please wait',delete_after=0)
    genderEmbed=discord.Embed(title="Question no.1", description="What's Your gender \n \n **Option:** `male` **or** `female`", color=0x631cba)
    genderEmbed.set_thumbnail(url=pfp)
    sentGender = await ctx.send(embed=genderEmbed)

    try:
      genderBmr = await self.bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
      if genderBmr:
        await sentGender.delete()
        await genderBmr.delete()
    
      ageEmbed=discord.Embed(title="Question no.2", description="What's Your age \n \n **e.g:** `16`", color=0x631cba)
      ageEmbed.set_thumbnail(url=pfp)
      sentAge = await ctx.send(embed=ageEmbed)
  
      ageBmr = await self.bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
      if ageBmr:
        await sentAge.delete()
        await ageBmr.delete()
    
      heightEmbed=discord.Embed(title="Question no.3", description="What's Your height (`In cm`) \n\n **Example:** `175`", color=0x631cba)
      heightEmbed.set_thumbnail(url=pfp)
      sentHeight = await ctx.send(embed=heightEmbed)
  
      heightBmr = await self.bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
      if heightBmr:
        await sentHeight.delete()
        await heightBmr.delete()

      weightEmbed=discord.Embed(title="Question no.4", description="What's Your weight (`In KG`) \n\n **Example:** `67`", color=0x631cba)
      weightEmbed.set_thumbnail(url=pfp)
      sentWeight = await ctx.send(embed=weightEmbed)
  
      weightBmr = await self.bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
      if weightBmr:
        await sentWeight.delete()
        await weightBmr.delete()

      final = BMR(genderBmr.content.lower(), float(ageBmr.content), float(weightBmr.content), float(heightBmr.content))
      L1 =f"**little or no exercise :**  `{round(final*1.2)}` Cal"
      L2 =f"**Exercise 1-3 times/week :**	 `{round(final*1.375)}` Cal"
      L3 =f"**Exercise 4-5 times/week	:**     `{round(final*1.55)}` Cal"
      L4 =f"**Daily exercise 3-4 times/week :** `{round(final*1.725)}` Cal"
      L5 =f"**Intense exercise 6-7 times/week :** `{round(final*1.8)}` Cal"
      L6 =f"**Very intense exercise daily	:**      `{round(final*1.9)}` Cal"

    
      finalEmbed=discord.Embed(title="Your BMR is..", description=f"BMR = **{final}** Calories/day \n \n{L1}\n{L2}\n{L3}\n{L4}\n{L5}\n{L6}", color=0x631cba)
      finalEmbed.set_thumbnail(url=pfp)

      await ctx.send(embed=finalEmbed)
    except asyncio.exceptions.TimeoutError:
      await ctx.send(f'**You took too long to respond** {Rosaria}')



def setup(bot):
	bot.add_cog(bmr(bot))