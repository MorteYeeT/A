
# bot.py
import os

import discord
prefix = '!'
responses = ['hi', 'Hi', 'HI', 'hI']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {client.user}!\n User id = {self.user.id}')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(prefix+ responses):
            await message.reply('Hello!', mention_author=True)

client = MyClient()

client.run('')
