import discord
from discord.ext import commands
from discord.commands import slash_command
from Emojies import bold,cursive,hollow,tiny1,tiny2,arrow2
from typing import Optional
from discord.commands import option



FONT = [
  "bold",
  "cursive",
  "hollow",
  "subscript",
  "superscript",
  "all"  
]

class font(commands.Cog,name='font'):
  def __init__(self,bot):
    self.bot = bot

  async def command_searcher(self: discord.AutocompleteContext):
    return [
      font for font in FONT
    ]

  async def get_commands(ctx: discord.AutocompleteContext):
    return [font for font in FONT if font.startswith(ctx.value.lower())]
    
    
  @slash_command(name = 'font', description="Changes the font of the given sentence")
  @option("fontname", description="Pick a font", autocomplete=get_commands)
  async def font(self, ctx, fontname:str,message:str,ephemeral:Optional[bool]=False):
    fontName = fontname

    convMess = ''
    error = False
    all = False
    match fontname:
      case "bold":
        convMess = ''
        for letter in message:   
          convMess += bold[letter]

      case "cursive":       
        convMess = ''
        for letter in message:          
          convMess += cursive[letter]
          
      case "hollow":
        convMess = ''
        for letter in message:
          convMess += hollow[letter]
          
      case "subscript":     
        convMess = ''
        for letter in message.upper():
          convMess += tiny1[letter]
          
      case "superscript":
        convMess = ''
        for letter in message:
          convMess += tiny2[letter]
          
      case "all":
        L1 = ''
        L2 = ''
        L3 = ''
        L4 = ''
        L5 = ''
        for letter in message:
          L1 += bold[letter]
        for letter in message:
          L2 += cursive[letter]
        for letter in message:
          L3 += hollow[letter]
        for letter in message:
          L4 += tiny1[letter.upper()]
        for letter in message:
          L5 += tiny2[letter]
        all = True
        error = True
      case _:
        embed=discord.Embed(title="",description="**\❌Invalid Font name\❌** \n Do `~help font` to learn more")
        await ctx.respond(embed=embed,ephemeral=ephemeral)
        error = True
        
    if not error:
      
      embed=discord.Embed(title=f'Normal {arrow2} {fontName}',description=f'\n \n**{convMess}**', color=0x631cba)
      await ctx.respond(embed=embed,ephemeral=ephemeral)
    elif all:
      embed=discord.Embed(title=f'Normal {arrow2} {fontName}',description=f'**{L1}\n{L2}\n{L3}\n{L4}\n{L5}\n\nMore Coming Soon!**', color=0x631cba)
      await ctx.respond(embed=embed,ephemeral=ephemeral)



def setup(bot):
	bot.add_cog(font(bot))