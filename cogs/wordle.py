import discord
from Emojies import greenEmoji,yellowEmoji,grayEmoji
from function import wordpick
from discord.ext import commands
from discord.commands import slash_command

class pageView(discord.ui.View):
  pages:int = 20
  current:int=1
  def __init__(self,arr,pfp):
    self.arr = arr
    self.pfp = pfp
    super().__init__()

  def create_embed(self,page,pfp):
    
    arr = page.split('\n')


    page = '\n'.join(['* **{}**'.format(str(i)) for i in arr])


    embed = discord.Embed(title='',description=f"# Wordlist\n{page}\n## `{self.current}/20`",color=0x631cba)
    embed.set_thumbnail(url=pfp)
    return embed

  def update_buttons(self):
    if self.current == 1:
      self.previous.disabled = True

  @discord.ui.button(label="|<",style=discord.ButtonStyle.primary)
  async def first(self,button: discord.ui.button, interaction: discord.Interaction):
    self.current = 1
    embed = self.create_embed(self.arr[0],self.pfp)
    
    await interaction.response.edit_message(embed=embed)

  
  
  @discord.ui.button(label="<",style=discord.ButtonStyle.gray)
  async def previous(self,button: discord.ui.button, interaction: discord.Interaction):
    if self.current >= 2:
      self.current -= 1
    else:
      return await interaction.response.send_message("This is the first page", ephemeral=True)
    embed = self.create_embed(self.arr[self.current-1],self.pfp)
    
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label=">",style=discord.ButtonStyle.gray)
  async def next(self,button: discord.ui.button, interaction: discord.Interaction):
    if self.current <= 19:
      
      self.current += 1
    else:
      return await interaction.response.send_message("This is the last page", ephemeral=True)
    embed = self.create_embed(self.arr[self.current-1],self.pfp)
    
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label=">|",style=discord.ButtonStyle.primary)
  async def last(self,button: discord.ui.button, interaction: discord.Interaction):
    self.current = 20
    embed = self.create_embed(self.arr[-1],self.pfp)
    
    await interaction.response.edit_message(embed=embed)

  


class wordle(commands.Cog,name='wordle',description='Guess a 5-letter word from hints'):

  def __init__(self,bot):
    self.bot = bot
  
  @slash_command(name='wordle',description='Guess a 5-letter word from hints')
  async def wordle(self,ctx):
    await ctx.respond("Please wait...", ephemeral=True)
    pfp = ctx.author.avatar
    attempt = 0
    word = wordpick().upper()
    guessLeft = 5
    guess = ''
    emoji = ''
    embed1 = discord.Embed(title='Wordle',description='Your goal is to guess a 5-letter word. Goodluck. \n \n Do `~help wordle` to learn more.', color=0x631cba)
    embed1.set_thumbnail(url=pfp)
    await ctx.send(embed=embed1)
    while guess != word and guessLeft >= 0:
     
      guess1 = await self.bot.wait_for('message',timeout=120, check=lambda message: message.author == ctx.author and message.channel == ctx.channel and len(message.clean_content) == 5)
        
      await guess1.delete()
      guess = guess1.content.upper()
      for i in range(5):
        for letter in guess[i]:
          if guess[i] == word[i]:
            emoji += greenEmoji[guess[i]]
          elif guess[i] in word:
            emoji += yellowEmoji[guess[i]]
          elif guess[i] != word[i]:
            emoji += grayEmoji[guess[i]]   
          else:
            return
      
      attempt += 1
      embed2 = discord.Embed(title='',description=f'{emoji}\n **{guessLeft} Guess Left**', color=0x631cba)
      embed2.set_thumbnail(url=pfp)
      embed2.set_author(name=f"{ctx.author.name}", icon_url=pfp)
      await ctx.send(embed=embed2)
      guessLeft -= 1

      if guess == word:
        guessLeft -= 10
      emoji = ''
      guess = ''
    
    sendW = ''
    sendL = ''
    win = 'WON'
    lost = 'LOST'
    for letter in win:
      sendW += greenEmoji[letter]
    for letter in lost:
      sendL += yellowEmoji[letter]
    if guess1.content.upper() == word:
      embed = discord.Embed(title='Wordle',description=f"{sendW} \n You **Win**.You guessed the word in **{attempt}** tries", color=0x631cba)
      await ctx.send(embed=embed)
    
    elif guessLeft <= 0 and guess1.content.upper() != word:
      embed = discord.Embed(title='Wordle',description=f'{sendL}\nYou **Lost**. The word was **{word}**. Better luck next time', color=0x631cba)
      embed.set_thumbnail(url=pfp)
      await ctx.send(embed=embed)
  

  
  
  @slash_command(name='wordlist',description='The complete wordlist for wordle')
  async def wordlist(self, ctx):
    pfp = ctx.author.avatar
    with open("words.txt") as f:
      wordlist = f.readlines()

    string1 = ''.join(wordlist[:25])
    string2 = ''.join(wordlist[25:50])
    string3 = ''.join(wordlist[50:75])
    string4 = ''.join(wordlist[75:100])
    string5 = ''.join(wordlist[100:125])
    string6 = ''.join(wordlist[125:150])
    string7 = ''.join(wordlist[150:175])
    string8 = ''.join(wordlist[175:200])
    string9 = ''.join(wordlist[200:225])
    string10 = ''.join(wordlist[225:250])
    string11 = ''.join(wordlist[250:275])
    string12 = ''.join(wordlist[275:300])
    string13 = ''.join(wordlist[300:325])
    string14 = ''.join(wordlist[325:350])
    string15 = ''.join(wordlist[350:375])
    string16 = ''.join(wordlist[375:400])
    string17 = ''.join(wordlist[400:425])
    string18 = ''.join(wordlist[425:450])
    string19 = ''.join(wordlist[450:475])
    string20 = ''.join(wordlist[475:501])

    
    pages = [string1,string2,string3,string4,
             string5,string6,string7,string8,
             string9,string10,string11,string12,
             string13,string14,string15,string16,
             string17,string18,string19,string20
            ]
        
    arr = pages[0].split('\n')


    page = '\n'.join(['* **{}**'.format(str(i)) for i in arr])


    embed = discord.Embed(title='',description=f"# Wordlist\n{page}\n## `1/20`",color=0x631cba)
    embed.set_thumbnail(url=pfp)
    await ctx.respond(embed=embed,view=pageView(pages,pfp))

def setup(bot):
	bot.add_cog(wordle(bot))