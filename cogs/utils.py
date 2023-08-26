import discord
from datetime import datetime
from typing import Optional
import time
from discord.ext import commands
from discord.commands import slash_command

class utils(commands.Cog,name='utils'):

  def __init__(self,bot):
    self.bot = bot
  


  @slash_command(name="serverinfo",description="Gives informations about the current server")
  async def server_info(self,ctx):
    await ctx.respond("Please wait...")
    embed = discord.Embed(title="Server information",
          colour=ctx.guild.owner.colour,
          timestamp=datetime.utcnow())

    embed.set_thumbnail(url=ctx.guild.icon)

    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
        len(list(filter(lambda m: str(m.status) == "offline", 
  ctx.guild.members)))]

    fields = [("ID", ctx.guild.id, True),
        ("Owner", ctx.guild.owner, True),
        ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
        ("Members", len(ctx.guild.members), True),
        ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
        ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
        ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
        ("Text channels", len(ctx.guild.text_channels), True),
        ("Voice channels", len(ctx.guild.voice_channels), True),
        ("Categories", len(ctx.guild.categories), True),
        ("Roles", len(ctx.guild.roles), True),
        ("Invites", len(await ctx.guild.invites()), True),
        ("\u200b", "\u200b", True)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)


  @slash_command(name="userinfo", description="gives info about the mentioned user")
  async def user_info(self,ctx, target: Optional[discord.Member]):
    target = target or ctx.author

    embed = discord.Embed(title="User information",
          colour=target.colour,
          timestamp=datetime.utcnow())

    embed.set_thumbnail(url=target.avatar)

    fields = [("Name", str(target), True),
        ("ID", target.id, True),
        ("Bot?", target.bot, True),
        ("Top role", target.top_role.mention, True),
        ("Status", str(target.status).title(), True),
        ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
        ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
        ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
        ("Boosted", bool(target.premium_since), True)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    await ctx.respond(embed=embed)


def setup(bot):
  bot.add_cog(utils(bot))