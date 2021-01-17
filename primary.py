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
    await message.channel.send(file = discord.File('qrcode_test.png'))

client.run(config.TOKEN)

