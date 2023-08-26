import discord
import time as t
from discord.ext import commands
from discord.commands import slash_command
from function import time_conv
import asyncio
from typing import Optional
from discord import Member

class mod(commands.Cog,name='mod'):

  def __init__(self,bot):
    self.bot = bot


  
  @slash_command(name='mute',description='This command mutes people.')
  @commands.has_permissions(administrator=True) #permissions
  async def mute(self, ctx, user:Member,time:Optional[str]= "1i",reason:Optional[str]=None):
    unixCode = int(t.time())
  
    mute_time= time_conv(time)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    print_time = unixCode + mute_time
    if role == None:
      await ctx.respond('Created a Mute role')
      role = await ctx.guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False))
      await role.edit(colour=0x000000)
      
    if role.position > ctx.author.top_role.position:
      return await ctx.respond('**:x: | That role is above your top role!**') 
    if role in user.roles:
      await ctx.respond(f"{user.mention} is already muted") 
    else:
      pfp = user.avatar
      await user.add_roles(role) #mutes the user
      embed=discord.Embed(title="Muted", description=f"Muted {user.mention} \n Unmuted: <t:{print_time}:R> \n Reason: {reason}", color=0x1c1c1c)
      embed.set_thumbnail(url=(pfp))
      await ctx.respond(embed=embed)
    
      await asyncio.sleep(mute_time) 
      await user.remove_roles(role)
      await ctx.send(f'{user.mention} was Unmuted <t:{unixCode}:R>') 


  

  @slash_command(name = 'unmute',description='unmutes users who have been muted before')
  @commands.has_permissions(administrator=True) #permissions
  async def unmute(self,ctx, user:Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    pfp = user.avatar

    if role.position > ctx.author.top_role.position:
      return await ctx.respond('**:x: | That role is above your top role!**') 
      
    if role not in user.roles:
      await ctx.respond(f"{user.mention} is already unmuted")
    
    else:
      await user.remove_roles(role)     
      embed = discord.Embed(title="unmute", description=f" unmuted {user.mention}",color=0x1c1c1c)
      embed.set_thumbnail(url=(pfp))
      await ctx.respond(embed=embed)


  

  
  @slash_command(name = 'kick',description='this command kicks users')
  @commands.has_permissions(administrator=True) #permissions
  async def kick(self, ctx, user:Member,reason:Optional[str]=None):
  
    pfp = user.avatar #gets user's pfp

    embedDM=discord.Embed(title="Kicked", description=f"You were Kicked from **{ctx.guild.name}** \n Reason: **{reason}**", color=0x1c1c1c) #sends this embed to the kicked user
    embedDM.set_thumbnail(url=(pfp))
  #if user == bot.user:
    #return
  #else:
    #await user.send(embed=embedDM)
    embed=discord.Embed(title="Kicked", description=f"{user.mention} was Kicked from **{ctx.guild.name}** \n Reason: **{reason}**", color=0x1c1c1c) #sends this embed in the ctx channl
    embed.set_thumbnail(url=(pfp))
    await ctx.respond(embed=embed)
    await user.kick(reason=reason) #kicks the user



  
  @slash_command(name = 'role',description='Assigns or Unassigns a role to user')
  @commands.has_permissions(administrator=True) #permissions
  async def role(self,ctx,role : discord.Role, user : Optional[Member]=None):

    user = ctx.author if user == None else user
    pfp = user.avatar
    if role.position > ctx.author.top_role.position: 
      return await ctx.respond('**:x: | That role is above your top role!**',ephemeral=True)
    if role in user.roles:
      try:
        await user.remove_roles(role) #removes the role if user already has
        embed=discord.Embed(title='',description=f"Removed {role} from {user.mention}")
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed)
      except:
        embed = discord.Embed(title='Permission Error',description="**I do not have the permission to do that**\n* That role's position is higher than mine",ephemeral=True)
        embed.set_thumbnail(url=pfp)
        return await ctx.respond(embed=embed)
    else:
      try:
        await user.add_roles(role) #adds role if not already has it
        embed=discord.Embed(title='',description=f"Added {role} from {user.mention}")
        embed.set_thumbnail(url=pfp)
        await ctx.respond(embed=embed)
      except:
        embed = discord.Embed(title='Permission Error',description="**I do not have the permission to do that**\n* That role's position is higher than mine", ephemeral=True)
        embed.set_thumbnail(url=pfp)
        return await ctx.respond(embed=embed)
  


  
def setup(bot):
	bot.add_cog(mod(bot))