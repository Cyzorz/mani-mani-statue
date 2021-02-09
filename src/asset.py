import discord
from path import Path

class Asset:
    @staticmethod
    def getFile(asset):
        return discord.File(open(Path.get(f"assets/{asset}"), "rb"), filename=asset.replace("/", "_"))