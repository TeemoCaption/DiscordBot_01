from quopri import encodestring
import discord
from discord.ext import commands
import json
import random


with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.all()
intents.members=True

bot=commands.Bot(command_prefix="! ",intents=intents)   #建置Discord機器人
#command_prefix=>打指令前的命令字首

@bot.command()
async def ping(ctx):     #打指令    ctx全名叫context
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
    
@bot.command()
async def photo(ctx):
    random_pic=random.choice(jdata["photo"])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.event     #機器人事件
#async def=>協程函式
async def on_ready():   
    print("Bot is online")
    
@bot.event  
async def on_member_join(member):     #成員加入
    channel=bot.get_channel(int(jdata['welcome_channel']))       #get_channel("頻道id")=>取得頻道
    await channel.send(f"{member} 跳進來了")      #發送訊息

@bot.event  
async def on_member_remove(member):     #成員離開
    channel=bot.get_channel(int(jdata['leave_channel']))       #get_channel("頻道id")=>取得頻道
    await channel.send(f"{member} 離開了")


bot.run(jdata['TOKEN'])  #執行機器人