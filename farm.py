from .. import loader, utils

class FarmMod(loader.Module):
    """EF mod."""
    strings = {'name': 'Farm'}

    async def watcher(self, message):
        try:
            if message.chat_id in {-100779130604}:
                if message.sender_id in {1254069556}:      
                    if "Завершить работу" in message.message:
                        await message.respond('завершить работу')
                    if "Поход в столовую" in message.message:
                        await message.respond('поход в столовую')
                    if "Покормить жабу" in message.message:
                        await message.respond('покормить жабу')
        except: pass