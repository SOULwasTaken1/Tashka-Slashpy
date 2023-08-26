import discord
from discord.commands import slash_command
from discord.ext import commands
import random
from discord.commands import Option
from Emojies import bar1,bar2,bar3,fbar1,fbar2,fbar3,cringe
from Emojies import Zhongli_cool, Ning_cool, Zhongli_ohno, Bannet
from discord import Member
from typing import Optional

class dank(commands.Cog,name='dank'):
  def __init__(self,bot):
    self.bot = bot
  

  @slash_command(name="highlow",description="Starts a guessing game with the given range")
  async def highlow(self,ctx, range:Option(int,required = False, default = 10000)):
    pfp = ctx.author.avatar
    secret_num = random.randint(1,range)
    attempts = 0
  
    embed1 = discord.Embed(title='', description=f"# Guess The Number\n## How To Play \n * I've thought of a number between **1** and **{range}** \n* You have **UNLIMITED** guesses \n* Some messages will be deleted to avoid spam \n* Your attempts will be tracked", color=0x631cba)
    guess = 0
    
    await ctx.respond(embed=embed1)
  
    while guess != secret_num:
      guessInput = await self.bot.wait_for('message',timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
      guessC = guessInput.content

      try:
        guess = int(guessC)
      except:
        
        embedE = discord.Embed(title='',description='# Invalid Input.\n ### Please type Send an integer number', color= 0xFF0000)
        await ctx.send(embed=embedE, delete_after=14)
        attempts -= 1
        

      embedL = discord.Embed(title='', description=f' Your guess: **{guess}** \n Try something **LOWER**', color=0x00FFFF)
    
      embedH = discord.Embed(title='', description=f' Your guess: **{guess}** \n Try something **HIGHER**', color=0xFFFF00)


      await guessInput.delete()
    
      if guess == secret_num:
        break
      elif guess <= secret_num:
        await ctx.send(embed=embedH, delete_after=14)
      elif guess >= secret_num:
        await ctx.send(embed=embedL, delete_after=14)
        

      
      attempts += 1

    embedW = discord.Embed(title='You Won', description=f'The number was: **{secret_num}** \n it took you **{attempts} guesses**', color=0x00FF00)
    embedW.set_thumbnail(url=pfp)
  
    await ctx.send(embed=embedW)

  @slash_command(name="pp",description="Generates user's pp with random size")
  async def pp(self,ctx, user:Optional[Member]):

    
    pp = '8'
    size = 0
    if user == None:
      pfp = ctx.author.avatar
      name = ctx.author.name
    
      if ctx.author.id == 801058284106678273: #soul
        size += 15
        size += random.randint(2,15)
      elif ctx.author.id == 726076022361030708: #dummy
        size += 3
        size -= random.randint(1,3)
      elif ctx.author.id == 695169282107113562: #damn
        size += 3
        size -= random.randint(1,3)
      elif ctx.author.id == 789416858478051330: #tababy
        size += 11
        size += random.randint(1,10)
      else:
        size += random.randint(1,15)
    elif user != None:
      pfp = user.avatar  
      name = user.display_name
      if user.id == 801058284106678273: #soul
        size += 15
        size += random.randint(2,15)
      elif user.id == 695169282107113562: #damn
        size += 3
        size -= random.randint(1,3)
      elif user.id == 726076022361030708: #dummy
        size += 3
        size -= random.randint(1,3)
      elif user.id == 971753818389905418: #tashka
        size += 25
        size += random.randint(5,17)
      elif user.id == 789416858478051330: #tababy
        size += 11
        size += random.randint(1,10)
      else:
        size += random.randint(1,15)

    for i in range(size):
      pp += '='
    pp += 'D'


    embed=discord.Embed(title=f"{name}'s pp", description=f'**{pp}**')
    embed.set_author(name=name, url=pfp, icon_url=pfp)
    await ctx.respond(embed=embed)

  @slash_command(name="coolrate",description="Tells you how cool you are. The rates are random")
  async def coolrate(self,ctx,user:Optional[Member]):
    if user == None:
      user = ctx.author
    else:
      user = user
    pfp = user.avatar

    b1 = bar1
    b2= bar2
    b3 = bar3
    fb1 = fbar1 
    fb2 = fbar2 
    fb3 = fbar3 
  
    bar = ''
    comment = ''
    rate = 0
    if user.id == 801058284106678273: #soul
      rate += 50 
      rate += random.randint(1,50)
      Chance = random.randint(1,5)
      if Chance == 2: #plus 
        rate += 74
        Super = random.randint(1,5)
        if Super == 1:
          rate += random.randint(200,500)
        else:
          rate += random.randint(1,300)
    elif user.id == 971753818389905418: #tashka
      rate += 100
      Chance = random.randint(1,5)
      if Chance == 2: #plus
        rate += 74
        Super = random.randint(1,9)
        if Super == 1:
          rate += random.randint(300,500)
        else:
          rate += random.randint(70,200)
    else: #everyone
      rate += random.randint(1,100)
      chance = random.randint(1,4)
      otherChance = random.randint(1,5)
      if chance == 1: # minus
        rate -= 87
        Super = random.randint(1,4)
        if Super == 1:
          rate -= random.randint(100,400)
        else:
          rate -= random.randint(23,83)
      if otherChance == 2: #plus
        rate += 74
        Super = random.randint(1,20)
        if Super == 1:
          rate += random.randint(1,500)
        else:
          rate += random.randint(1,50)
    
    if rate <0 and rate >= -30:
      bar += f'{b1}{b2}{b2}{b2}{b2}{b3}'
      comment += f'You are so cringe {cringe}'
    elif rate <= -30 and rate >= -100:
      bar += f'{b3}{b1}{b2}{b2}{b2}{b2}{b3}'
      comment += f'You are so cringe {cringe}' 
    elif rate < -100:
      bar += f'{b2}{b3}{b1}{b2}{b2}{b2}{b2}{b3}'
      comment += f'No one likes you. Everyone hates you {cringe}'
    elif rate >= 0 and rate < 25:
      bar += f'{fb1}{b2}{b2}{b2}{b2}{b3}'
      comment += f'You are kinda cringe {cringe}'
    elif rate >= 20 and rate < 50:
      bar += f'{fb1}{fb2}{b2}{b2}{b2}{b3}'
      comment += f'You are kinda lame {Zhongli_ohno}'
    elif rate >= 50 and rate < 60:
      bar += f'{fb1}{fb2}{fb2}{b2}{b2}{b3}'
      comment += f'Mid. {Bannet}'
    elif rate >= 60 and rate < 75:
      bar += f'{fb1}{fb2}{fb2}{fb2}{b2}{b3}'
      comment += f' You are above average {Ning_cool}'
    elif rate >= 75 and rate < 80:
      bar += f'{fb1}{fb2}{fb2}{fb2}{fb2}{b3}'
      comment += f'You are kinda cool {Ning_cool}'
    elif rate >= 80 and rate <= 99:
      bar += f'{fb1}{fb2}{fb2}{fb2}{fb2}{b3}'
      comment += f'You are super cool {Zhongli_cool}'
    elif rate >= 100 and rate <=101:
      bar += f'{fb1}{fb2}{fb2}{fb2}{fb2}{fb3}'
      comment += f'You are the Coolest {Zhongli_cool}'
    elif rate >= 101 and rate <= 200:
      bar += f'{fb1}{fb2}{fb2}{fb2}{fb2}{fb3}{fb1}'
      comment += f'You are the Coolest {Zhongli_cool}'     
    elif rate >=200:
      bar += f'{fb1}{fb2}{fb2}{fb2}{fb2}{fb3}{fb1}{fb2}{fb2}'
      comment += f'You are beyond cool. Everyone loves you {Zhongli_cool}'

    embed = discord.Embed(title='CoolRate', description=f'{bar} **{rate}%** \n \n **{comment}**')
    embed.set_thumbnail(url=pfp)

    await ctx.respond(embed=embed)
  


def setup(bot):
	bot.add_cog(dank(bot))