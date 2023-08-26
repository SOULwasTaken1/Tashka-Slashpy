import discord
import time
from Emojies import bar1, bar2,bar3,fbar1,fbar2,fbar3
from function import Eightball
from discord.ext import commands
import random
from discord.commands import slash_command
from typing import Optional

class Menu(discord.ui.View):
  def __init__(self,cont):
    super().__init__()
    self.value = None
    self.cont = cont

  @discord.ui.button(label="Show Options",style=discord.ButtonStyle.grey)
  async def menu1(self,button:discord.ui.Button,interaction:discord.Interaction):
    await interaction.response.send_message(self.cont,ephemeral=True)
    
  
    

class eight_ball(commands.Cog,name='eight_ball'):

  def __init__(self,bot):
    self.bot = bot
  

  @slash_command(name="eightball",description="The magicall 8ball will tell you everything...")
  async def eightball(self, ctx,question:str,ephemeral:Optional[bool]=False):
    reply = random.choice(Eightball)

    embed1 = discord.Embed(title='8Ball',
                         description='**Thinking.**'+
                         f'\n** {bar1}{bar2}{bar2}{bar2}{bar2}{bar3} 0% **'
                         , color=0x631cba)

    embed2 = discord.Embed(title='8Ball',
                         description='**Thinking. .**'+
                         f'\n** {fbar1}{bar2}{bar2}{bar2}{bar2}{bar3} 12.5%  **'
                         , color=0x631cba)
    embed3 = discord.Embed(title='8Ball',
                         description='**Thinking. . .**'+
                         f'\n** {fbar1}{fbar2}{bar2}{bar2}{bar2}{bar3} 25% **'
                         , color=0x631cba)
    embed4 = discord.Embed(title='8Ball',
                         description='**Thinking. .**'+
                         f'\n**{fbar1}{fbar2}{fbar2}{bar2}{bar2}{bar3} 43.75% **'
                         , color=0x631cba)
    embed5 = discord.Embed(title='8Ball',
                         description='**Thinking.**'+
                         f'\n**{fbar1}{fbar2}{fbar2}{fbar2}{bar2}{bar3} 56.25%** '
                         , color=0x631cba)
    embed6 = discord.Embed(title='8Ball',
                         description='**Thinking. .**'+
                         f'\n**{fbar1}{fbar2}{fbar2}{fbar2}{fbar2}{bar3} 75%  ** '
                         , color=0x631cba)
    embed7 = discord.Embed(title='8Ball',
                         description='**Thinking. . .**'+
                         f'\n**{fbar1}{fbar2}{fbar2}{fbar2}{fbar2}{fbar3} 100%  **'
                         , color=0x631cba)

    embed8 = discord.Embed(title='8Ball',
                         description=f'\n**{fbar1}{fbar2}{fbar2}{fbar2}{fbar2}{fbar3} 100% **'+
                         f'\n \n**{reply}**', color=0x631cba)

  
    thinking = await ctx.respond(embed=embed1,ephemeral=ephemeral)
    time.sleep(0.3)
    await thinking.edit_original_response(embed=embed2)
    time.sleep(0.4)
    await thinking.edit_original_response(embed=embed3)
    time.sleep(0.5)
    await thinking.edit_original_response(embed=embed4)
    time.sleep(0.6)
    await thinking.edit_original_response(embed=embed5)
    time.sleep(0.3)
    await thinking.edit_original_response(embed=embed6)
    time.sleep(0.2)
    await thinking.edit_original_response(embed=embed7)
    time.sleep(0.2)
    await thinking.edit_original_response(embed=embed8)



  
  @slash_command(name="choose",description="Helps you to choose from upto 10 different options.")
  async def choose(self,ctx,
                   choice1,
                   choice2:Optional[str]=None,
                   choice3:Optional[str]=None,
                   choice4:Optional[str]=None,
                   choice5:Optional[str]=None,
                   choice6:Optional[str]=None,
                   choice7:Optional[str]=None,
                   choice8:Optional[str]=None,
                   choice9:Optional[str]=None,
                   choice10:Optional[str]=None
                  ):
                    
    pfp = ctx.author.avatar
    ChoiceList = []
    if choice1 !=None:
      ChoiceList.append(choice1)
    if choice2 != None:
      ChoiceList.append(choice2)
    if choice3 != None:
      ChoiceList.append(choice3)
    if choice4 != None:
      ChoiceList.append(choice4)
    if choice5 != None:
      ChoiceList.append(choice5)
    if choice6 != None:
      ChoiceList.append(choice6)
    if choice7 != None:
      ChoiceList.append(choice7)
    if choice8 != None:
      ChoiceList.append(choice8)
    if choice9 != None:
      ChoiceList.append(choice9)
    if choice10 != None:
      ChoiceList.append(choice10)
    cont = f"""
```py
ChoiceList = [{', '.join(['"{}"'.format(str(item)) for item in ChoiceList])}]

``` 
    """
    view = Menu(cont)

    embed = discord.Embed(title='', description=f'**I choose** {random.choice(ChoiceList)}')
    embed.set_thumbnail(url=pfp)
    embed.set_author(name=f"{ctx.author.name}", icon_url=pfp)
    await ctx.respond(embed=embed,view=view)



def setup(bot):
	bot.add_cog(eight_ball(bot))