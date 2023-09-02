import discord
from discord.ext import commands
from discord.commands import slash_command
from typing import Optional
import json
from datetime import datetime
import pytz
import os
from discord.commands import option
from function import count_lines
from itertools import groupby
import matplotlib.pyplot as plt

CHANGE = ["add","remove"]


class pageView(discord.ui.View):
  current:int=1
  def __init__(self,arr,pfp,pages,title):
    self.arr = arr
    self.pfp = pfp
    self.pages = pages
    self.title = title
    super().__init__()

  def create_embed(self,page,pfp):
    

    embed = discord.Embed(title=self.title,description=f"```py\n{page}\n```\n{self.current}/{self.pages}")
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
    if self.current == self.pages:
      return await interaction.response.send_message("This is the last page", ephemeral=True)
    elif self.current < self.pages:
      
      self.current += 1
      embed = self.create_embed(self.arr[self.current-1],self.pfp)
      await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label=">|",style=discord.ButtonStyle.primary)
  async def last(self,button: discord.ui.button, interaction: discord.Interaction):
    self.current = self.pages
    embed = self.create_embed(self.arr[-1],self.pfp)
    
    await interaction.response.edit_message(embed=embed)

class funds(commands.Cog,name='funds'):

  def __init__(self,bot):
    self.bot = bot
    


  async def command_searcher(self: discord.AutocompleteContext):
    return [
      change for change in CHANGE
    ]
  
  async def get_commands(ctx: discord.AutocompleteContext):
    return [change for change in CHANGE if change.startswith(ctx.value.lower())]  

  @slash_command()
  @option("change", autocomplete=get_commands)
  async def fund(self, ctx,change, amount,note:Optional[str]="No notes",ephemeral:Optional[bool]=False):
    TIME = datetime.now(pytz.timezone('Asia/Dhaka'))
    id = ctx.author.id
    filename = f"Lbalance/{id}.json"
    if not os.path.exists(filename):
      data = [{"id": id,"balance": 0,"privacy-level":0,"create-date": str(TIME)[0:10]}]
      with open(f"Lbalance/{id}.json", "w") as q:
        json.dump(data, q)
        
    with open(f"Lbalance/{id}.json", "r") as f:
      data = json.loads(f.read())
      balance = int(data["balance"])
    
      sign = ''
      string = ''
      if change == "add":
        balance += int(amount)
        string = f"Successfully Added {int(amount)}, **Current Balance**: `{balance}`"
        sign = '+'
        C = 0x00ff00
      elif change == "remove":
        balance -= int(amount)
        string = f"Successfully **Removed** {int(amount)}, **Current Balance**: `{balance}`"
        sign = '-'
        C = 0xff0000

    data["balance"] = balance
    with open(f"Lbalance/{id}.json", "w") as q:
      json.dump(data, q)
    
    
    date = str(TIME)[0:10]
    time = str(TIME)[11:18]
    result = {
      'amount':f"{sign}{int(amount)}",
      "time": time,
      "date": date,
      "note": note,
      "current": balance
    }
    
    with open(f"Lfund/{id}.json", "r") as k:
      existing_data = json.load(k)

    existing_data.append(result)

    with open(f'Lfund/{id}.json', 'w') as file:
      json.dump(existing_data, file, indent=2)
      
    t = f"{ctx.author}'s Balance {balance}"
    embed=discord.Embed(title=t,description=string,color=C)
    await ctx.respond(embed=embed,ephemeral=ephemeral)
  @slash_command()
  async def fund_log(self,ctx,user:Optional[discord.User]=None,ephemeral:Optional[bool]=False):
    if user != None:
      name = user.name
      id = user.id
      pfp = user.avatar
      if not os.path.exists(f"Lfund/{id}.json"):
        embed = discord.Embed(description=f"**{name}** does not have any fund records",color=0xff0000)
        return await ctx.respond(embed=embed,ephemeral=ephemeral)
      with open(f"Lbalance/{id}.json", "r") as f:
        data = json.loads(f.read())
        balance = int(data["balance"])
        if data["privacy-level"] == 1:
          embed=discord.Embed(description="This user wants to hide their Fund logs", color=0xff0000)
          return await ctx.respond(embed=embed,ephemeral=ephemeral)
        
        
    else:
      name = ctx.author.name
      id = ctx.author.id
      pfp = ctx.author.avatar
      if not os.path.exists(f"Lfund/{id}.json"):
        embed = discord.Embed(description="you do not have any fund records",color=0xff0000)
        return await ctx.respond(embed=embed,ephemeral=ephemeral)
      with open(f"Lbalance/{id}.json", "r") as f:
        data = json.loads(f.read())
        balance = int(data["balance"])
    
    with open(f"Lfund/{id}.json", "r") as k:
      string = k.read()
      embed = discord.Embed(title=f"Balance of {name}: {balance}",description=f"```json\n{string}\n```")
      embed.set_thumbnail(url=pfp)
      if count_lines(string) >= 42:

        
        json_file_path = f'Lfund/{id}.json'
        with open(json_file_path, 'r') as f:
            json_lines = f.readlines()
        
        lines_per_page = 42
        page_data = [json_lines[i:i+lines_per_page] for i in range(0, len(json_lines), lines_per_page)]
        
        pages = []
        
        for page_num, page_lines in enumerate(page_data, start=1):
          
            page_json = ''.join(page_lines)
            pages.append(page_json)
        pagecount = len(pages)
        title = f"{name}'s Balance: {balance}"
        embed = discord.Embed(title=title,description=f"```py\n{pages[0]}\n```\n1/3")
        embed.set_thumbnail(url=pfp)
        return await ctx.respond(embed=embed,ephemeral=ephemeral,view=pageView(pages,pfp,pagecount,title))
        
      else:
        return await ctx.respond(embed=embed,ephemeral=ephemeral)
  
  @slash_command()
  async def fund_privacy(self,ctx,private:bool,ephemeral:Optional[bool]=False):
    id = ctx.author.id
    if not os.path.exists(f"Lfund/{id}.json"):
      embed=discord.Embed(description="You do not have any fund records yet.",color=0xff0000)
      return await ctx.respond(embed=embed,ephemeral=ephemeral)
    if private:
      
      with open(f"Lbalance/{id}.json", "r") as q:
        data = json.load(q)
      data["privacy-level"] = 1
      
      with open(f"Lbalance/{id}.json", "w") as p:
        json.dump(data,p)
      embed=discord.Embed(description="Your fund records are now private",color=0x00ff00)
      return await ctx.respond(embed=embed,ephemeral=ephemeral)
    elif not private:
      with open(f"Lbalance/{id}.json", "r") as q:
        data = json.load(q)
      data["privacy-level"] = 0
    
      with open(f"Lbalance/{id}.json", "w") as p:
        json.dump(data,p)
      embed=discord.Embed(description="Your fund records are no longer private",color=0x00ff00)
      return await ctx.respond(embed=embed,ephemeral=ephemeral)
  
  @slash_command()
  async def fund_delete(self,ctx,ephemeral:Optional[bool]=False):
    id = ctx.author.id
    pfp = ctx.author.avatar
    if not os.path.exists(f"Lfund/{id}.json"):
      embed = discord.Embed(title="",description="You do not have any fund records yet.")
      embed.set_thumbnail(url=pfp)
      return await ctx.respond(embed=embed,ephemeral=ephemeral)
      
    embed = discord.Embed(title="",description="# Are you Sure?\nReply `y`/`n`")
    embed.set_thumbnail(url=pfp)
    await ctx.respond(embed=embed,ephemeral=ephemeral)
    
    reply = await self.bot.wait_for('message',timeout=120, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    if reply.content == "y":
      os.remove(f"Lbalance/{id}.json")
      os.remove(f"Lfund/{id}.json")
      embed = discord.Embed(title="",description=" All of your Fund records have been deleted.")
      await ctx.send(embed=embed)
      embed.set_thumbnail(url=pfp)
      
    if reply.content == "n":
      embed = discord.Embed(description="Cancelled the deletion process")
      embed.set_thumbnail(url=pfp)
      await ctx.send(embed=embed)
    await reply.delete()
    
  @slash_command()
  async def fund_graph(self,ctx,user:Optional[discord.User]=None,ephemeral:Optional[bool]=False):
    if user != None:
      name = user.name
      id = user.id
      pfp = user.avatar
      if not os.path.exists(f"Lfund/{id}.json"):
        embed = discord.Embed(description=f"**{name}** does not have any fund records",color=0xff0000)
        return await ctx.respond(embed=embed,ephemeral=ephemeral)
      with open(f"Lbalance/{id}.json", "r") as f:
        data = json.loads(f.read())
        balance = int(data["balance"])
        if data["privacy-level"] == 1:
          embed=discord.Embed(description="This user wants to hide their Fund logs", color=0xff0000)
          return await ctx.respond(embed=embed,ephemeral=ephemeral)
        
        
    else:
      name = ctx.author.name
      id = ctx.author.id
      pfp = ctx.author.avatar
      if not os.path.exists(f"Lfund/{id}.json"):
        embed = discord.Embed(description="you do not have any fund records",color=0xff0000)
        return await ctx.respond(embed=embed,ephemeral=ephemeral)
      with open(f"Lbalance/{id}.json", "r") as f:
        data = json.loads(f.read())
        balance = int(data["balance"])

    with open(f"Lfund/{id}.json", 'r') as q:
      data = json.load(q)
    grouped_data = {key: list(group) for key, group in groupby(data, key=lambda x: x['date'])}

    dates = []
    current_values = []
    
    for date, items in grouped_data.items():
        dates.append(date)
        current_values.append(items[-1]['current'])  
    
    
    plt.style.use('dark_background')
    
    
    plt.plot(dates, current_values, color='white', marker='o', label='Current Amount')
    
    for i, item in enumerate(grouped_data.values()):
        amount = item[-1]['amount'][1:]
        plt.annotate(f'{amount}', (dates[i], current_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='white', bbox=dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0'))
    
    plt.title('Current Amount Over Time')
    plt.xlabel('Date')
    plt.ylabel('Current Amount')
    
    plt.xticks(rotation=45)
    
    plt.legend(frameon=False)
    
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    plt.savefig('output_graph.png', dpi=300,transparent=True, bbox_inches='tight')
    plt.close()

    await ctx.respond(content="",file=discord.File("output_graph.png"),ephemeral=ephemeral)
    os.remove("output_graph.png")
    
    
      


def setup(bot):
  bot.add_cog(funds(bot))
