import discord
from discord.ext import commands
import os
import openai
from discord.commands import slash_command

class gpt(commands.Cog,name='gpt'):

  def __init__(self,bot):
    self.bot = bot

  @slash_command(name='ask',description='Ask Chat GPT any questions. Warning: This might not work if my API key expires')
  async def ask(self,ctx,prompt:str):
    await ctx.respond("Please wait...",delete_after=1)
    openai.api_key = os.environ['OPENAI_KEY']
    try:
      completion= openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages = [
          {'role':'user','content':prompt}
        ],
        temperature = 0.4,
      )
      embed=discord.Embed(description=completion['choices'][0]['message']['content'],color=0x631cba)
      
      await ctx.send(embed=embed)
    except openai.error.RateLimitError as e:
      str = f"```diff\n-openai.error.RateLimtEror: {e}\n ```"
      embed=discord.Embed(description=f"**The API key most likely expired**\n**Contact SOUL#7093 to let him know**\n**Note:I will reply to all of you.**\n**Error**\n\n{str}",color=0xF800)
      await ctx.respond(embed=embed)
    except Exception as err:

      embed=discord.Embed(description=f"```diff\n-{type(err).__name__} was raised: {err}\n```",color=0xF800)
      await ctx.respond(embed=embed)

    

def setup(bot):
	bot.add_cog(gpt(bot))
