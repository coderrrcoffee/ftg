#<3 title: NedoGhoul
#<3 pic: https://img.icons8.com/fluency/48/000000/dota.png
#<3 desc: Покажет участникам чата, что ты - гуль!


import io, inspect
from .. import loader, utils
from asyncio import sleep
from math import floor

@loader.tds
class GULMod(loader.Module):
    """Я - недогуль!"""
    strings = {'name': 'NedoGhoul', 
    'iamghoul': "Я - недогуль!"}
    
    async def гульcmd(self, message):
        x = 1414
        emojies = ["[Я ГУЛЬ!] ", "[ГУЛЬГУЛЬГУЛЬ] ", "[Я ЗАГУЛИЛСЯ] ", "[ТЫ ГУЛЬ!] ", "[ГУЛЬ СДОХ] "]
        await message.edit(self.strings('iamghoul', message))
        await sleep(2)
        while x > 0:
            await message.edit(emojies[floor((1414 - x) / (1414 / len(emojies)))] + str(x) + " - 7 = " + str(x-7))
            x -= 7
            await sleep(1)
