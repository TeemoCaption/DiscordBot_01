import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="!")   #建置Discord機器人
#command_prefix=>打指令前的命令字首

@bot.event     #機器人事件
#async def=>協程函式
async def on_ready():   
    print("Bot is online")
    
@bot.event  
async def on_member_join(member):     #成員加入
    channel=bot.get_channel(939909732922175579)       #get_channel("頻道id")=>取得頻道
    await channel.send(f"{member} 跳進來了")      #發送訊息
    
async def on_member_remove(member):     #成員離開
    channel=bot.get_channel(939910394682691625)       #get_channel("頻道id")=>取得頻道
    await channel.send(f"{member} 離開了")


bot.run("OTM5ODI0NzQ4NzY0OTg3Mzk1.Yf-eAQ.LSic8tLpDdIeD9CyYBSQm2BKZpY")  #執行機器人