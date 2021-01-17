import discord
from database import DB
from discord.ext import commands
import qrcodegen as qr
import config

client = commands.Bot(command_prefix="m!")

async def on_ready(self):
    print(self.user.name + "has been deployed!")
    await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"QR codes!"))

@client.command()
async def qrcode(message):
    qr.qrGen.create()
    #result = database.thing.find_points()
    await message.channel.send(file = discord.File('qrcode_test.png'))
    #if i == False:
    #    i = 0
    #    return True
    DB.update_points(1, message.author.id)
    #await message.channel.send(f"{message.author.mention} has {i} points!")

client.run(config.TOKEN)

