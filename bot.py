import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="!")   #建置Discord機器人
#command_prefix=>打指令前的命令字首

@bot.event     #機器人事件
#async def=>協程函式
async def on_ready():     #功能
    print("Bot is online")


bot.run("OTM5ODI0NzQ4NzY0OTg3Mzk1.Yf-eAQ.noKSn13eIDibjLHqi79dNHnXR-A")  #執行機器人