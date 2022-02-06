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
    print(f"{member} 跳進來了！")
    
async def on_member_remove(member):     #成員離開
    print(f"{member} 離開了！")


bot.run("OTM5ODI0NzQ4NzY0OTg3Mzk1.Yf-eAQ.9RxcH8jhR_PYByZgUIqmUBbw0u0")  #執行機器人