import discord
import database
from discord.ext import commands
import qrcodegen as qr
import config

client = commands.Bot(command_prefix="m!")

async def on_ready(self):
    print(self.user.name + "has been deplyed!")
    await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"QR codes!"))

@client.command()
async def qrcode(message):
    qr.qrGen.create()
    result = database.thing.find_points(message.author.id, 0)
    await message.channel.send(f'{result}', file = discord.File('qrcode_test.png'))
    #if i == False:
    #    i = 0
    #    return True
    #database.DB.update_points(int(message.author.id, int(i) + 1))
    #await message.channel.send(f"{message.author.mention} has {i} points!")

client.run(config.TOKEN)

