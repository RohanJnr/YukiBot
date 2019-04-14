from aiohttp import AsyncResolver, ClientSession, TCPConnector
import logging
import os
import socket
from datetime import datetime

from discord.ext import commands


logger = logging.getLogger(__name__)
# All the cogs that are to be loaded on launch
cogs = ['bot.cogs.owners',
        'bot.cogs.moderation',
        'bot.cogs.info',
        'bot.cogs.minigames']


class Yuki(commands.Bot):
    def __init__(self):
        self.lime = 0x04ff00

        super().__init__(command_prefix='?',  # Needs to be changed to allow for database setup, simply a holder ATM
                         description='Description Here!')

    async def on_ready(self):
        self.http_session = ClientSession(
            connector=TCPConnector(resolver=AsyncResolver(), family=socket.AF_INET)
        )
        for cog in cogs:
            try:
                self.load_extension(cog)
            except Exception as e:
                logger.error(f'Failed to load extension: {cog}\n{e}')

        logger.info(f'Client Logged in at {datetime.now()}')
        logger.info(f'Logged in as : {self.user.name}')
        logger.info(f'ID : {self.user.id}')

    def run(self):
        super().run(os.environ.get('TOKEN'), reconnect=True)


if __name__ == '__main__':
    bot = Yuki()
    bot.run()
