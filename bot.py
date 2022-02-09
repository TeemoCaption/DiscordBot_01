from quopri import encodestring
from unicodedata import name
import discord
from discord.ext import commands
import json
import os


with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
    
intents=discord.Intents.all()
intents.members=True

bot=commands.Bot(command_prefix="!",intents=intents)   #建置Discord機器人
#command_prefix=>打指令前的命令字首


@bot.event     #機器人事件
#async def=>協程函式
async def on_ready():   
    print("Bot is online")
    

@bot.command()
async def load(ctx,extension):    #cog---load載入類別
    bot.load_extension(f'cmds.{extension}')   #載入外部檔
    await ctx.send(f"loaded {extension} 成功！")
    
@bot.command()
async def unload(ctx,extension):     #cog---unload刪除類別
    bot.unload_extension(f'cmds.{extension}')   #載入外部檔
    await ctx.send(f"Un-loaded {extension} 成功！")
    
@bot.command()
async def reload(ctx,extension):     #動態修改指令後載入至類別
    bot.reload_extension(f'cmds.{extension}')   #載入外部檔
    await ctx.send(f"Re-loaded {extension} 成功！")


for Filename in os.listdir('./cmds'):      #遍歷cmds資料夾
    if(Filename.endswith('.py')):     #如果檔名為.py
        bot.load_extension(f'cmds.{Filename[:-3]}')    #從檔名開頭取到倒數第三個字

if __name__=="__main__":
    bot.run(jdata['TOKEN'])  #執行機器人

